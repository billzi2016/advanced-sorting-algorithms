def counting_sort(values: list[int]) -> list[int]:
    # 空数组直接返回空数组。
    if not values:
        return []

    # 统计值域范围，支持包含负数的输入。
    min_value = min(values)
    max_value = max(values)
    counts = [0] * (max_value - min_value + 1)

    # counts[i] 表示值 i + min_value 出现的次数。
    for value in values:
        counts[value - min_value] += 1

    # 按值从小到大展开计数结果。
    result = []
    for index, count in enumerate(counts):
        result.extend([index + min_value] * count)

    return result
