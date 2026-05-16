def selection_sort(values: list[int]) -> list[int]:
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
