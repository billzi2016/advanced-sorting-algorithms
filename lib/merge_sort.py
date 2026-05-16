def merge_sort(values: list[int]) -> list[int]:
    # 递归终止条件：空数组或单元素数组天然有序。
    if len(values) <= 1:
        return values[:]

    # 将数组拆成左右两部分，分别递归排序。
    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    # 合并两个已经有序的子数组。
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = 0
    j = 0

    # 两个指针分别扫描左右数组，每次取较小值放入结果。
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 其中一边扫描完成后，另一边剩余元素本身已经有序。
    result.extend(left[i:])
    result.extend(right[j:])
    return result
