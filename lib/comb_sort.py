"""梳排序。

梳排序可以看作冒泡排序的改进版。它先用较大的 gap 比较远距离元素，
尽早消除“乌龟元素”（很小但位于数组后部的元素），随后逐步缩小 gap，
最终退化为 gap=1 的冒泡式扫描。
"""


def comb_sort(values: list[int]) -> list[int]:
    """使用递减 gap 的交换策略返回升序副本。"""

    # 复制输入，避免排序过程修改原数组。
    result = values[:]
    gap = len(result)
    shrink = 1.3
    sorted_pass = False

    while not sorted_pass:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_pass = True

        # gap 大于 1 时交换远距离逆序对；gap 等于 1 时确认最终有序。
        for i in range(0, len(result) - gap):
            if result[i] > result[i + gap]:
                result[i], result[i + gap] = result[i + gap], result[i]
                sorted_pass = False

    return result
