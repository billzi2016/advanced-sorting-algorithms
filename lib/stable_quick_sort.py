"""稳定快速排序。

普通原地快速排序会交换相等元素，通常不稳定。
本实现用 left/mid/right 三个新列表分区，相等元素按原始扫描顺序进入 mid，
因此牺牲 O(n) 额外空间换取稳定性和更直观的教学实现。
"""


def stable_quick_sort(values: list[int]) -> list[int]:
    """使用稳定三列表分区返回升序副本。"""

    # 空数组或单元素数组天然有序，直接返回副本。
    if len(values) <= 1:
        return values[:]

    # 选择中间元素作为基准值。
    pivot = values[len(values) // 2]
    left = []
    mid = []
    right = []

    # 按原始顺序把元素放入 left、mid、right 三个数组。
    # 相等元素进入 mid，因此相对顺序不会被打乱。
    for value in values:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            mid.append(value)

    # 递归排序左右数组，最后按 left + mid + right 合并。
    return stable_quick_sort(left) + mid + stable_quick_sort(right)
