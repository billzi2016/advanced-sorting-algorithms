def insertion_sort(values: list[int]) -> list[int]:
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
