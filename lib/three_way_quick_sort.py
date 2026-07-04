"""三路快速排序。

三路分区把数组一次划分成小于、等于、大于基准的三段。
当输入包含大量重复值时，等于基准的元素不再进入递归区间，
因此通常比普通二路快速排序更稳。
"""


def three_way_quick_sort(values: list[int]) -> list[int]:
    """使用 Dijkstra 三路分区返回升序副本。"""

    # 在副本上原地分区，保持外部接口不修改输入数组。
    result = values[:]
    _sort(result, 0, len(result) - 1)
    return result


def _sort(values: list[int], left: int, right: int) -> None:
    """在闭区间 [left, right] 内执行三路快速排序。

    循环不变量:
        [left, lt) 小于 pivot；
        [lt, i) 等于 pivot；
        (gt, right] 大于 pivot；
        [i, gt] 是尚未分类的区域。
    """

    if left >= right:
        return

    pivot = values[(left + right) // 2]
    # [left, lt) 小于 pivot， [lt, i) 等于 pivot， (gt, right] 大于 pivot。
    lt = left
    i = left
    gt = right

    while i <= gt:
        if values[i] < pivot:
            values[lt], values[i] = values[i], values[lt]
            lt += 1
            i += 1
        elif values[i] > pivot:
            # 换到右侧的新值还没检查，所以这里不移动 i。
            values[i], values[gt] = values[gt], values[i]
            gt -= 1
        else:
            i += 1

    _sort(values, left, lt - 1)
    _sort(values, gt + 1, right)
