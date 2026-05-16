def shell_sort(values: list[int]) -> list[int]:
    # 复制输入，避免排序过程修改原数组。
    result = values[:]
    gap = len(result) // 2

    # 按 gap 分组做插入排序，逐步缩小 gap。
    while gap > 0:
        for i in range(gap, len(result)):
            current = result[i]
            j = i

            # 对同一个 gap 子序列执行插入排序的右移过程。
            while j >= gap and result[j - gap] > current:
                result[j] = result[j - gap]
                j -= gap

            result[j] = current

        gap //= 2

    return result
