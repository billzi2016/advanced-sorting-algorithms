import argparse
import random

from benchmarks.benchmark import (
    parse_patterns,
    parse_sizes,
    print_benchmark_table,
    run_benchmark,
    write_rows,
)
from lib.registry import AlgorithmSpec, get_algorithm, iter_algorithms


def build_correctness_cases(
    random_cases: int,
    max_length: int,
    seed: int,
) -> list[list[int]]:
    # 固定样例覆盖边界输入和典型分布，随机样例负责补充更大的输入空间。
    cases = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 3, 3],
        [4, -1, 0, -7, 8, 3, 3, -1],
        [10, 9, 8, 1, 2, 7, 6, 3, 5, 4],
        [100, -100, 50, -50, 0, 25, -25],
        [42, 17, 8, 99, 23, 4, 16, 15, 15, 0, -3, -100, 2048],
    ]

    rng = random.Random(seed)
    value_bound = max(10, max_length * 4)

    for _ in range(random_cases):
        length = rng.randint(0, max_length)
        cases.append([rng.randint(-value_bound, value_bound) for _ in range(length)])

    for length in (8, 32, max_length):
        if length <= 0:
            continue
        # 近乎有序数组用于检查算法对局部扰动输入的处理是否正确。
        base = list(range(length))
        for _ in range(max(1, length // 16)):
            left = rng.randrange(length)
            right = rng.randrange(length)
            base[left], base[right] = base[right], base[left]
        cases.append(base)

    return cases


def select_algorithms(keys: str | None) -> list[AlgorithmSpec]:
    if not keys:
        return list(iter_algorithms())

    selected = []
    for key in keys.split(","):
        cleaned = key.strip()
        if cleaned:
            selected.append(get_algorithm(cleaned))
    return selected


def list_algorithms() -> None:
    headers = [
        "key",
        "family",
        "stable",
        "best",
        "average",
        "worst",
        "space",
    ]
    rows = [
        [
            spec.key,
            spec.family,
            "yes" if spec.stable else "no",
            spec.best_time,
            spec.average_time,
            spec.worst_time,
            spec.space,
        ]
        for spec in iter_algorithms()
    ]
    _print_table(headers, rows)


def verify_algorithms(
    algorithms: list[AlgorithmSpec],
    random_cases: int,
    max_length: int,
    seed: int,
) -> bool:
    cases = build_correctness_cases(random_cases, max_length, seed)

    for spec in algorithms:
        for index, case in enumerate(cases):
            # 每次传入副本，既验证排序结果，也验证算法不会修改调用方输入。
            source = case[:]
            actual = spec.function(source)
            expected = sorted(case)

            if source != case:
                print(f"[FAIL] {spec.key}: mutated input at case #{index}")
                print(f"input: {case}")
                print(f"after: {source}")
                return False

            if actual != expected:
                print(f"[FAIL] {spec.key}: wrong result at case #{index}")
                print(f"input:    {case}")
                print(f"expected: {expected}")
                print(f"actual:   {actual}")
                return False

        print(f"[PASS] {spec.key}")

    print(f"All {len(algorithms)} sorting algorithms passed {len(cases)} cases.")
    return True


def _print_table(headers: list[str], rows: list[list[str]]) -> None:
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]

    print("  ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> argparse.Namespace:
    # 子命令保持轻量：list 看元数据，verify 做正确性验证，benchmark 做本地性能采样。
    parser = argparse.ArgumentParser(
        description="Sorting algorithm verification and benchmarking toolkit.",
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List available algorithms and metadata.")

    verify_parser = subparsers.add_parser("verify", help="Run correctness checks.")
    verify_parser.add_argument("--algorithms", help="Comma-separated algorithm keys.")
    verify_parser.add_argument("--random-cases", type=int, default=100)
    verify_parser.add_argument("--max-length", type=int, default=128)
    verify_parser.add_argument("--seed", type=int, default=20260517)

    benchmark_parser = subparsers.add_parser("benchmark", help="Run local benchmarks.")
    benchmark_parser.add_argument("--algorithms", help="Comma-separated algorithm keys.")
    benchmark_parser.add_argument("--sizes", default="32,128,512")
    benchmark_parser.add_argument(
        "--patterns",
        default="random,sorted,reversed,duplicates,nearly_sorted",
    )
    benchmark_parser.add_argument("--repeat", type=int, default=3)
    benchmark_parser.add_argument("--seed", type=int, default=20260517)
    benchmark_parser.add_argument("--output", help="Optional .csv or .json output path.")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    command = args.command or "verify"

    try:
        if command == "list":
            list_algorithms()
        elif command == "verify":
            algorithms = select_algorithms(args.algorithms)
            if not verify_algorithms(
                algorithms,
                args.random_cases,
                args.max_length,
                args.seed,
            ):
                raise SystemExit(1)
        elif command == "benchmark":
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
        else:
            raise SystemExit(f"unknown command: {command}")
    except KeyError as exc:
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":
    main()
