"""归并排序。

归并排序是稳定的分治排序：先递归拆分数组，再把两个有序子数组合并。
它的时间复杂度稳定为 O(n log n)，代价是需要 O(n) 额外空间保存合并结果。
"""


def merge_sort(values: list[int]) -> list[int]:
    """返回 values 的升序副本。"""

    # 递归终止条件：空数组或单元素数组天然有序。
    if len(values) <= 1:
        return values[:]

    # 将数组拆成左右两部分，分别递归排序。
    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    # 合并两个已经有序的子数组。
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """稳定合并两个已经升序排列的列表。

    当左右元素相等时优先取 left 中的元素，因此可以保持原始相对顺序。
    """

    result = []
    i = 0
    j = 0

    # 两个指针分别扫描左右数组，每次取较小值放入结果。
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 其中一边扫描完成后，另一边剩余元素本身已经有序。
    result.extend(left[i:])
    result.extend(right[j:])
    return result
