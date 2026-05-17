# Advanced Sorting Algorithms

Advanced Sorting Algorithms 是一个面向排序算法实现、验证和性能分析的 Python 项目。项目将常见排序、分治排序、分布式排序和混合排序统一到同一套接口中，提供可复现的正确性验证和本地 benchmark 工具，便于比较不同算法在数据分布、输入规模和稳定性约束下的行为差异。

## 项目目标

- 实现一组覆盖面较完整的排序算法，保持统一输入输出约定。
- 为每个算法记录稳定性、复杂度、空间开销、适用场景和输入约束。
- 使用确定性样例和随机样例验证排序结果与 `sorted()` 一致。
- 提供可配置 benchmark，用固定随机种子复现不同数据分布下的运行时间。
- 保持项目结构清晰，便于继续扩展算法、测试和实验维度。

## 核心功能

- 排序算法库：所有算法位于 `lib/`，函数接收 `list[int]`，返回新的有序列表，不修改输入数组。
- 算法注册表：`lib/registry.py` 统一管理算法函数、复杂度、稳定性和适用说明。
- 命令行入口：`main.py` 支持列出算法、运行正确性验证和执行 benchmark。
- 单元测试：`tests/` 覆盖空数组、重复值、负数、逆序、近乎有序和随机输入。
- Benchmark：`benchmarks/benchmark.py` 支持多输入规模、多数据分布、多轮重复和 CSV/JSON 输出。

## 已实现算法

| 算法 | 类型 | 平均时间复杂度 | 最坏时间复杂度 | 空间复杂度 | 稳定 |
| --- | --- | --- | --- | --- | --- |
| Bubble Sort | exchange | O(n^2) | O(n^2) | O(1) | 是 |
| Cocktail Shaker Sort | exchange | O(n^2) | O(n^2) | O(1) | 是 |
| Comb Sort | exchange | O(n^2 / 2^p) | O(n^2) | O(1) | 否 |
| Selection Sort | selection | O(n^2) | O(n^2) | O(1) | 否 |
| Insertion Sort | insertion | O(n^2) | O(n^2) | O(1) | 是 |
| Shell Sort | insertion | 依赖 gap 序列 | O(n^2) | O(1) | 否 |
| Merge Sort | merge | O(n log n) | O(n log n) | O(n) | 是 |
| Tim Sort | hybrid | O(n log n) | O(n log n) | O(n) | 是 |
| Quick Sort | partition | O(n log n) | O(n^2) | O(log n) | 否 |
| Stable Quick Sort | partition | O(n log n) | O(n^2) | O(n) | 是 |
| Three-way Quick Sort | partition | O(n log n) | O(n^2) | O(log n) | 否 |
| Dual-pivot Quick Sort | partition | O(n log n) | O(n^2) | O(log n) | 否 |
| Intro Sort | hybrid | O(n log n) | O(n log n) | O(log n) | 否 |
| Heap Sort | selection | O(n log n) | O(n log n) | O(1) | 否 |
| Tree Sort | tree | O(n log n) | O(n^2) | O(n) | 否 |
| Counting Sort | distribution | O(n + k) | O(n + k) | O(k) | 是 |
| Radix Sort | distribution | O(dn) | O(dn) | O(n) | 是 |
| Bucket Sort | distribution | O(n + k) | O(n^2) | O(n + k) | 是 |

## 技术栈

- Python 3.10+
- 标准库 `argparse`、`random`、`time`、`statistics`、`csv`、`json`
- 标准库 `unittest`
- 无第三方依赖

## 项目结构

```text
advanced-sorting-algorithms/
├── README.md
├── .gitignore
├── main.py
├── benchmarks/
│   ├── __init__.py
│   └── benchmark.py
├── lib/
│   ├── __init__.py
│   ├── registry.py
│   ├── bubble_sort.py
│   ├── bucket_sort.py
│   ├── cocktail_sort.py
│   ├── comb_sort.py
│   ├── counting_sort.py
│   ├── dual_pivot_quick_sort.py
│   ├── heap_sort.py
│   ├── insertion_sort.py
│   ├── intro_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── radix_sort.py
│   ├── selection_sort.py
│   ├── shell_sort.py
│   ├── stable_quick_sort.py
│   ├── three_way_quick_sort.py
│   ├── tim_sort.py
│   └── tree_sort.py
└── tests/
    └── test_sorting_algorithms.py
```

## 运行方式

列出全部算法和元数据：

```bash
python3 main.py list
```

运行正确性验证：

```bash
python3 main.py verify
```

只验证指定算法：

```bash
python3 main.py verify --algorithms intro_sort,tim_sort,three_way_quick_sort
```

运行本地 benchmark：

```bash
python3 main.py benchmark --sizes 32,128,512 --repeat 3
```

将 benchmark 结果写入文件：

```bash
python3 main.py benchmark --sizes 64,256,1024 --output benchmarks/results/latest.csv
```

运行单元测试：

```bash
python3 -B -m unittest discover -s tests
```

## 正确性验证

验证逻辑会覆盖：

- 空数组和单元素数组
- 已排序数组和逆序数组
- 重复元素
- 负数、零和正数混合
- 大小值跨度较大的整数
- 固定随机种子生成的随机数组
- 近乎有序数组
- 输入数组不被修改的接口约束

所有算法的输出都会与 Python 内置 `sorted()` 结果对比。

## Benchmark 说明

Benchmark 支持以下数据分布：

- `random`：整数随机分布
- `sorted`：完全有序
- `reversed`：完全逆序
- `duplicates`：重复值密集
- `nearly_sorted`：局部扰动的近乎有序数组

默认 benchmark 不保存结果，只在终端输出表格。需要沉淀实验数据时，可以通过 `--output` 写入 `.csv` 或 `.json`。仓库不内置固定性能结论，避免将不同机器、不同解释器版本下的运行时间混为一谈。

## 当前进度

- 已完成 18 个排序算法实现。
- 已完成统一算法注册表。
- 已完成 CLI 入口、正确性验证和 benchmark 工具。
- 已完成 `unittest` 测试用例。
- 已补充 README 和 `.gitignore`。

## 后续计划

- 增加外部排序示例，用分块、临时文件和多路归并处理内存受限场景。
- 增加更细粒度的 benchmark 报告，包括比较次数、交换次数和内存峰值。
- 增加稳定性验证的对象排序版本，区分值相同但原始位置不同的记录。
- 增加可视化输出，将不同算法在输入规模和分布上的表现生成图表。
