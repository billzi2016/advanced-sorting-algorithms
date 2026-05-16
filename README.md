# Advanced Sorting Algorithms

这是一个 Python 排序算法实现项目。

项目目标很直接：`lib/` 中每个文件实现一个排序算法，`main.py` 统一测试所有算法的正确性，并与 Python 内置 `sorted()` 的结果进行对比。

## 项目结构

```text
advanced-sorting-algorithms/
├── README.md
├── .gitignore
├── main.py
└── lib/
    ├── __init__.py
    ├── bubble_sort.py
    ├── bucket_sort.py
    ├── counting_sort.py
    ├── heap_sort.py
    ├── insertion_sort.py
    ├── merge_sort.py
    ├── quick_sort.py
    ├── radix_sort.py
    ├── selection_sort.py
    ├── shell_sort.py
    └── stable_quick_sort.py
```

## 已实现算法

| 算法 | 平均时间复杂度 | 空间复杂度 | 是否稳定 |
| --- | --- | --- | --- |
| 冒泡排序 | O(n^2) | O(1) | 是 |
| 选择排序 | O(n^2) | O(1) | 否 |
| 插入排序 | O(n^2) | O(1) | 是 |
| 希尔排序 | 取决于 gap 序列 | O(1) | 否 |
| 归并排序 | O(n log n) | O(n) | 是 |
| 快速排序 | O(n log n) | O(log n) | 否 |
| 稳定快速排序 | O(n log n) | O(n) | 是 |
| 堆排序 | O(n log n) | O(1) | 否 |
| 计数排序 | O(n + k) | O(k) | 是 |
| 基数排序 | O(dn) | O(n) | 是 |
| 桶排序 | O(n + k) | O(n + k) | 取决于桶内排序 |

## 运行方式

```bash
python3 main.py
```

预期输出：

```text
[PASS] bubble_sort
[PASS] selection_sort
[PASS] insertion_sort
[PASS] shell_sort
[PASS] merge_sort
[PASS] quick_sort
[PASS] stable_quick_sort
[PASS] heap_sort
[PASS] counting_sort
[PASS] radix_sort
[PASS] bucket_sort
All sorting algorithms passed correctness tests.
```

## 测试说明

`main.py` 会测试以下输入场景：

- 空数组
- 单元素数组
- 已排序数组
- 逆序数组
- 重复元素
- 负数
- 正负混合
- 普通无序数组

所有算法都会与 `sorted()` 的输出结果进行比较。

## 说明

- 每个算法文件只负责一个排序算法。
- 所有排序函数接收 `list[int]`，返回排序后的新列表。
- 不修改输入数组，便于测试和对比。
- 如果需要写代码注释，统一使用中文。
- 本项目用于算法实现、工程组织和正确性验证。
