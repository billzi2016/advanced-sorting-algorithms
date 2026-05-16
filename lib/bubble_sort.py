def bubble_sort(values: list[int]) -> list[int]:
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
