"""选择排序。

选择排序每轮从未排序区间中找到最小值，并把它交换到当前边界位置。
它的比较次数始终是 O(n^2)，但交换次数最多 O(n)，因此适合作为
“少交换、多比较”的基础排序示例。
"""


def selection_sort(values: list[int]) -> list[int]:
    """返回 values 的升序副本。"""

    # 复制输入，避免排序过程修改原数组。
    result = values[:]

    # 每一轮从未排序区间中选择最小值，放到当前位置。
    for i in range(len(result)):
        min_index = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j

        # 选择排序通过交换完成放置，因此不是稳定排序。
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]

    return result
