def intro_sort(values: list[int]) -> list[int]:
    result = values[:]
    if len(result) <= 1:
        return result

    # 深度上限约束快速排序递归深度，超过后切换堆排序避免 O(n^2) 退化。
    max_depth = 2 * (len(result).bit_length() - 1)
    _intro_sort(result, 0, len(result) - 1, max_depth)
    # 小区间留到最后统一插入排序，减少递归和分区开销。
    _insertion_sort_range(result, 0, len(result) - 1)
    return result


def _intro_sort(values: list[int], left: int, right: int, depth_limit: int) -> None:
    while right - left > 16:
        if depth_limit == 0:
            # 快速排序分区过深时，直接用堆排序保证最坏 O(n log n)。
            _heap_sort_range(values, left, right)
            return

        depth_limit -= 1
        pivot_index = _partition(values, left, right)

        # 先递归较小分区，较大分区用循环继续处理，降低调用栈深度。
        if pivot_index - left < right - pivot_index:
            _intro_sort(values, left, pivot_index - 1, depth_limit)
            left = pivot_index + 1
        else:
            _intro_sort(values, pivot_index + 1, right, depth_limit)
            right = pivot_index - 1


def _partition(values: list[int], left: int, right: int) -> int:
    # 三数取中降低已排序、逆序等输入下选到极端基准的概率。
    pivot_index = _median_of_three(values, left, (left + right) // 2, right)
    pivot = values[pivot_index]
    values[pivot_index], values[right] = values[right], values[pivot_index]

    store_index = left
    for i in range(left, right):
        if values[i] < pivot:
            values[i], values[store_index] = values[store_index], values[i]
            store_index += 1

    values[store_index], values[right] = values[right], values[store_index]
    return store_index


def _median_of_three(values: list[int], a: int, b: int, c: int) -> int:
    if values[a] < values[b]:
        if values[b] < values[c]:
            return b
        if values[a] < values[c]:
            return c
        return a

    if values[a] < values[c]:
        return a
    if values[b] < values[c]:
        return c
    return b


def _heap_sort_range(values: list[int], left: int, right: int) -> None:
    size = right - left + 1

    # 先在指定区间内建最大堆，再逐步把堆顶放到区间尾部。
    for root in range(size // 2 - 1, -1, -1):
        _sift_down(values, left, root, size)

    for end in range(size - 1, 0, -1):
        values[left], values[left + end] = values[left + end], values[left]
        _sift_down(values, left, 0, end)


def _sift_down(values: list[int], offset: int, root: int, size: int) -> None:
    while True:
        child = root * 2 + 1
        if child >= size:
            return

        if child + 1 < size and values[offset + child] < values[offset + child + 1]:
            child += 1

        if values[offset + root] >= values[offset + child]:
            return

        values[offset + root], values[offset + child] = (
            values[offset + child],
            values[offset + root],
        )
        root = child


def _insertion_sort_range(values: list[int], left: int, right: int) -> None:
    # 插入排序在小区间和近乎有序输入上常数开销较低。
    for i in range(left + 1, right + 1):
        current = values[i]
        j = i - 1

        while j >= left and values[j] > current:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = current
