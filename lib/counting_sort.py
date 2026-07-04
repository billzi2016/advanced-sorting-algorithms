"""计数排序。

计数排序适合整数值域不大的场景。它统计每个值出现次数，再按值从小到大展开。
本实现通过 min_value 偏移支持负数，但如果最大值和最小值差距极大，
counts 数组会占用大量空间。
"""


def counting_sort(values: list[int]) -> list[int]:
    """使用值域计数返回升序列表。"""

    # 空数组直接返回空数组。
    if not values:
        return []

    # 统计值域范围，支持包含负数的输入。
    min_value = min(values)
    max_value = max(values)
    counts = [0] * (max_value - min_value + 1)

    # counts[i] 表示值 i + min_value 出现的次数。
    for value in values:
        counts[value - min_value] += 1

    # 按值从小到大展开计数结果。
    result = []
    for index, count in enumerate(counts):
        result.extend([index + min_value] * count)

    return result
