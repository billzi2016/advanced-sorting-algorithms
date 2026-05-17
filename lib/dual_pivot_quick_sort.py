def dual_pivot_quick_sort(values: list[int]) -> list[int]:
    # 在副本上排序，统一满足“返回新列表、不修改输入”的项目约定。
    result = values[:]
    _sort(result, 0, len(result) - 1)
    return result


def _sort(values: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    if values[left] > values[right]:
        values[left], values[right] = values[right], values[left]

    # 两个基准把数组划分为三段：小于 low、位于两基准之间、大于 high。
    pivot_low = values[left]
    pivot_high = values[right]
    lt = left + 1
    gt = right - 1
    i = lt

    while i <= gt:
        if values[i] < pivot_low:
            values[i], values[lt] = values[lt], values[i]
            lt += 1
            i += 1
        elif values[i] > pivot_high:
            # 先从右侧找到一个不大于高基准的元素，再与当前位置交换。
            while values[gt] > pivot_high and i < gt:
                gt -= 1

            values[i], values[gt] = values[gt], values[i]
            gt -= 1

            # 交换回来的元素可能小于低基准，需要再放入左侧分区。
            if values[i] < pivot_low:
                values[i], values[lt] = values[lt], values[i]
                lt += 1

            i += 1
        else:
            i += 1

    lt -= 1
    gt += 1
    # 把两个基准放回分区边界，之后递归处理三段子区间。
    values[left], values[lt] = values[lt], values[left]
    values[right], values[gt] = values[gt], values[right]

    _sort(values, left, lt - 1)
    _sort(values, lt + 1, gt - 1)
    _sort(values, gt + 1, right)
