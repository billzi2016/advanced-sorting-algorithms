"""快速排序。

本模块实现原地分区版本的快速排序，但对外仍返回输入副本，保持项目统一接口。
分区时选择中间元素作为基准，能降低已排序或逆序输入下选到极端基准的概率。
"""


def quick_sort(values: list[int]) -> list[int]:
    """使用双指针快速排序返回升序副本。"""

    # 复制输入，然后在副本上执行原地快速排序。
    result = values[:]
    _quick_sort_in_place(result, 0, len(result) - 1)
    return result


def _quick_sort_in_place(values: list[int], left: int, right: int) -> None:
    """在闭区间 [left, right] 内原地执行快速排序。"""

    # 区间长度小于 2 时，不需要继续排序。
    if left >= right:
        return

    # 选取中间元素作为基准值，降低有序输入下的退化概率。
    pivot = values[(left + right) // 2]
    i = left
    j = right

    # 双指针从两端向中间移动，把小值放左边，大值放右边。
    while i <= j:
        while values[i] < pivot:
            i += 1
        while values[j] > pivot:
            j -= 1

        if i <= j:
            values[i], values[j] = values[j], values[i]
            i += 1
            j -= 1

    # 分别递归处理左右两个分区。
    if left < j:
        _quick_sort_in_place(values, left, j)
    if i < right:
        _quick_sort_in_place(values, i, right)
