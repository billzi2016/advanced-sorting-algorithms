def bucket_sort(values: list[int]) -> list[int]:
    # 空数组或单元素数组天然有序，直接返回副本。
    if len(values) <= 1:
        return values[:]

    # 根据最小值和最大值确定桶的映射范围。
    min_value = min(values)
    max_value = max(values)

    if min_value == max_value:
        return values[:]

    # 桶数量使用 sqrt(n)，在简单实现中兼顾空间和分布。
    bucket_count = max(1, int(len(values) ** 0.5))
    buckets = [[] for _ in range(bucket_count)]
    value_range = max_value - min_value

    # 将每个值按比例映射到对应桶中。
    for value in values:
        index = int((value - min_value) * (bucket_count - 1) / value_range)
        buckets[index].append(value)

    # 每个桶内部排序后，再按桶顺序合并。
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result
