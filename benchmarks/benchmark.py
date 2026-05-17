import argparse
import csv
import json
import random
import statistics
import sys
import time
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    # 允许直接执行 benchmarks/benchmark.py，而不要求调用方手动设置 PYTHONPATH。
    sys.path.insert(0, str(PROJECT_ROOT))

from lib.registry import AlgorithmSpec, get_algorithm, iter_algorithms


def parse_sizes(value: str) -> list[int]:
    sizes = [int(item.strip()) for item in value.split(",") if item.strip()]
    if not sizes:
        raise ValueError("at least one size is required")
    if any(size < 0 for size in sizes):
        raise ValueError("sizes must be non-negative")
    return sizes


def parse_patterns(value: str) -> list[str]:
    patterns = [item.strip() for item in value.split(",") if item.strip()]
    supported = {"random", "sorted", "reversed", "duplicates", "nearly_sorted"}
    unknown = sorted(set(patterns) - supported)
    if unknown:
        raise ValueError(f"unsupported patterns: {', '.join(unknown)}")
    return patterns


def select_algorithms(value: str | None) -> list[AlgorithmSpec]:
    if not value:
        return list(iter_algorithms())
    return [get_algorithm(item.strip()) for item in value.split(",") if item.strip()]


def build_dataset(pattern: str, size: int, rng: random.Random) -> list[int]:
    # 所有数据集由外部传入的 rng 生成，保证相同 seed 下可复现。
    if pattern == "random":
        bound = max(10, size * 4)
        return [rng.randint(-bound, bound) for _ in range(size)]

    if pattern == "sorted":
        return list(range(size))

    if pattern == "reversed":
        return list(range(size, 0, -1))

    if pattern == "duplicates":
        values = [-8, -3, 0, 1, 1, 2, 5, 8]
        return [values[rng.randrange(len(values))] for _ in range(size)]

    if pattern == "nearly_sorted":
        values = list(range(size))
        swaps = max(1, size // 20) if size else 0
        # 少量随机交换模拟真实系统里常见的局部乱序输入。
        for _ in range(swaps):
            left = rng.randrange(size)
            right = rng.randrange(size)
            values[left], values[right] = values[right], values[left]
        return values

    raise ValueError(f"unsupported pattern: {pattern}")


def run_benchmark(
    algorithms: list[AlgorithmSpec],
    sizes: list[int],
    patterns: list[str],
    repeat: int,
    seed: int,
) -> list[dict[str, Any]]:
    if repeat <= 0:
        raise ValueError("repeat must be positive")

    rows = []

    for size in sizes:
        for pattern in patterns:
            # 不同 size/pattern 使用独立随机流，避免算法执行顺序影响数据生成。
            dataset_rng = random.Random(f"{seed}:{pattern}:{size}")
            dataset = build_dataset(pattern, size, dataset_rng)
            expected = sorted(dataset)

            for spec in algorithms:
                timings = []

                for _ in range(repeat):
                    # 每轮都复制输入，避免前一轮排序结果污染后一轮 benchmark。
                    source = dataset[:]
                    start = time.perf_counter()
                    actual = spec.function(source)
                    elapsed_ms = (time.perf_counter() - start) * 1000

                    if source != dataset:
                        raise AssertionError(f"{spec.key} mutated benchmark input")
                    if actual != expected:
                        raise AssertionError(f"{spec.key} produced invalid result")

                    timings.append(elapsed_ms)

                rows.append(
                    {
                        "algorithm": spec.key,
                        "family": spec.family,
                        "pattern": pattern,
                        "size": size,
                        "repeat": repeat,
                        "min_ms": min(timings),
                        "mean_ms": statistics.fmean(timings),
                        "max_ms": max(timings),
                    }
                )

    return rows


def print_benchmark_table(rows: list[dict[str, Any]]) -> None:
    headers = [
        "algorithm",
        "pattern",
        "size",
        "repeat",
        "min_ms",
        "mean_ms",
        "max_ms",
    ]
    formatted_rows = [
        [
            str(row["algorithm"]),
            str(row["pattern"]),
            str(row["size"]),
            str(row["repeat"]),
            f"{row['min_ms']:.3f}",
            f"{row['mean_ms']:.3f}",
            f"{row['max_ms']:.3f}",
        ]
        for row in rows
    ]
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in formatted_rows))
        for index in range(len(headers))
    ]

    print("  ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("  ".join("-" * width for width in widths))
    for row in formatted_rows:
        print("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def write_rows(rows: list[dict[str, Any]], output: str) -> None:
    output_path = Path(output)
    # 输出目录通常是本地实验产物目录，按需创建但不写入仓库默认数据。
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.suffix == ".json":
        with output_path.open("w", encoding="utf-8") as file:
            json.dump(rows, file, ensure_ascii=False, indent=2)
        return

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "algorithm",
                "family",
                "pattern",
                "size",
                "repeat",
                "min_ms",
                "mean_ms",
                "max_ms",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run sorting algorithm benchmarks.")
    parser.add_argument("--algorithms", help="Comma-separated algorithm keys.")
    parser.add_argument("--sizes", default="32,128,512")
    parser.add_argument(
        "--patterns",
        default="random,sorted,reversed,duplicates,nearly_sorted",
    )
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260517)
    parser.add_argument("--output", help="Optional .csv or .json output path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = run_benchmark(
        algorithms=select_algorithms(args.algorithms),
        sizes=parse_sizes(args.sizes),
        patterns=parse_patterns(args.patterns),
        repeat=args.repeat,
        seed=args.seed,
    )

    if args.output:
        write_rows(rows, args.output)
        print(f"Benchmark results written to {args.output}")
    else:
        print_benchmark_table(rows)


if __name__ == "__main__":
    main()
