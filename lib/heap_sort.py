"""堆排序。

堆排序先把数组原地调整成最大堆，然后反复把堆顶最大值交换到末尾。
它不是稳定排序，但额外空间为 O(1)，并且最坏时间复杂度稳定为 O(n log n)。
"""


def heap_sort(values: list[int]) -> list[int]:
    """使用最大堆策略返回升序副本。"""

    # 复制输入，避免排序过程修改原数组。
    result = values[:]
    n = len(result)

    # 从最后一个非叶子节点开始，把数组调整成最大堆。
    for i in range(n // 2 - 1, -1, -1):
        _heapify(result, n, i)

    # 每次把堆顶最大值交换到末尾，再恢复剩余区间的最大堆性质。
    for end in range(n - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        _heapify(result, end, 0)

    return result


def _heapify(values: list[int], heap_size: int, root: int) -> None:
    """修复以 root 为根的子堆，使其重新满足最大堆性质。

    调用前假设 root 的左右子树已经是最大堆，因此只需要把 root
    沿较大孩子方向向下交换，直到局部堆性质恢复。
    """

    # 假设左右子树已经满足堆性质，只修复 root 位置。
    largest = root
    left = root * 2 + 1
    right = root * 2 + 2

    # 找出 root、左孩子、右孩子中的最大值。
    if left < heap_size and values[left] > values[largest]:
        largest = left

    if right < heap_size and values[right] > values[largest]:
        largest = right

    # 如果最大值不是 root，就交换并继续向下修复。
    if largest != root:
        values[root], values[largest] = values[largest], values[root]
        _heapify(values, heap_size, largest)
