def radix_sort(values: list[int]) -> list[int]:
    # 空数组直接返回空数组。
    if not values:
        return []

    # 基数排序天然处理非负整数；这里把负数单独取绝对值排序。
    negatives = [-value for value in values if value < 0]
    non_negatives = [value for value in values if value >= 0]

    sorted_negatives = _radix_sort_non_negative(negatives)
    sorted_non_negatives = _radix_sort_non_negative(non_negatives)

    # 负数绝对值越大，实际值越小，所以需要反转后再加回负号。
    return [-value for value in reversed(sorted_negatives)] + sorted_non_negatives


def _radix_sort_non_negative(values: list[int]) -> list[int]:
    # 只处理非负整数。
    result = values[:]
    if not result:
        return []

    exp = 1
    max_value = max(result)

    # 从个位开始，逐位执行稳定的计数排序。
    while max_value // exp > 0:
        result = _counting_sort_by_digit(result, exp)
        exp *= 10

    return result


def _counting_sort_by_digit(values: list[int], exp: int) -> list[int]:
    counts = [0] * 10
    output = [0] * len(values)

    # 统计当前数位 0-9 的出现次数。
    for value in values:
        digit = (value // exp) % 10
        counts[digit] += 1

    # 转换为前缀和，用来确定每个元素的输出位置。
    for i in range(1, 10):
        counts[i] += counts[i - 1]

    # 反向遍历保证同一数位下的元素相对顺序不变。
    for value in reversed(values):
        digit = (value // exp) % 10
        output[counts[digit] - 1] = value
        counts[digit] -= 1

    return output
