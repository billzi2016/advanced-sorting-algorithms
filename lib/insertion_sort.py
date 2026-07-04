"""插入排序。

插入排序维护左侧有序区间，每次把当前元素插入到正确位置。
它在小数组和近乎有序数组上很高效，也是 TimSort、IntroSort 等混合排序
常用的小区间处理组件。
"""


def insertion_sort(values: list[int]) -> list[int]:
    """使用稳定插入排序返回升序副本。"""

    # 复制输入，避免排序过程修改原数组。
    result = values[:]

    # 维护左侧有序区间，把当前元素插入到正确位置。
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        # 将比当前元素大的值整体右移，给 current 留出插入位置。
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result
