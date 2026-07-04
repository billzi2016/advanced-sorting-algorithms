"""冒泡排序。

冒泡排序通过相邻元素比较和交换，把当前未排序区间的最大值逐轮推到末尾。
它是稳定排序；这里加入提前终止标记，当某一轮没有交换时说明数组已经有序。
"""


def bubble_sort(values: list[int]) -> list[int]:
    """返回 values 的升序副本，不修改调用方传入的列表。"""

    # 复制输入，避免排序过程修改原数组。
    result = values[:]
    n = len(result)

    # 每一轮把当前未排序区间中的最大值交换到末尾。
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True

        # 如果一整轮没有发生交换，说明数组已经有序。
        if not swapped:
            break

    return result
