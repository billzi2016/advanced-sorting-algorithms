"""简化版 TimSort。

TimSort 利用真实数据中常见的自然有序片段（run），先识别 run，
再用二分插入排序扩展短 run，最后按栈规则稳定归并。
本实现保留核心教学思路，不追求完整 CPython TimSort 的所有工程优化。
"""


def tim_sort(values: list[int]) -> list[int]:
    """识别自然 run 并稳定归并，返回升序副本。"""

    result = values[:]
    n = len(result)
    if n <= 1:
        return result

    # 简化版 TimSort：识别自然 run，短 run 用二分插入排序扩展，再按规则归并。
    min_run = _min_run_length(n)
    runs: list[tuple[int, int]] = []
    start = 0

    while start < n:
        run_end = _count_run(result, start, n)
        run_length = run_end - start
        forced_end = min(n, start + max(min_run, run_length))

        # 将当前 run 扩展到 min_run 附近，减少后续归并层数。
        _binary_insertion_sort(result, start, forced_end, run_end)
        runs.append((start, forced_end - start))
        _merge_collapse(result, runs)
        start = forced_end

    _merge_force_collapse(result, runs)
    return result


def _min_run_length(n: int) -> int:
    """计算简化 TimSort 使用的 min_run 长度。"""

    # 与 TimSort 思路一致，把初始 run 控制在便于平衡归并的范围。
    remainder = 0
    while n >= 64:
        remainder |= n & 1
        n >>= 1
    return n + remainder


def _count_run(values: list[int], start: int, end: int) -> int:
    """从 start 开始识别一个递增或递减 run，并返回 run 结束位置。"""

    if start + 1 == end:
        return end

    run_end = start + 2
    if values[start + 1] < values[start]:
        # 递减 run 反转成递增 run，后续统一做稳定归并。
        while run_end < end and values[run_end] < values[run_end - 1]:
            run_end += 1
        values[start:run_end] = reversed(values[start:run_end])
    else:
        while run_end < end and values[run_end] >= values[run_end - 1]:
            run_end += 1

    return run_end


def _binary_insertion_sort(
    values: list[int],
    start: int,
    end: int,
    sorted_start: int,
) -> None:
    """把 [sorted_start, end) 中的元素插入到 [start, i) 的有序区间。

    插入点用二分查找确定；元素移动仍然是线性的，但比较次数更少。
    """

    if sorted_start <= start:
        sorted_start = start + 1

    for i in range(sorted_start, end):
        current = values[i]
        left = start
        right = i

        # 用二分查找插入点，移动次数不变，但比较次数更少。
        while left < right:
            mid = (left + right) // 2
            if current < values[mid]:
                right = mid
            else:
                left = mid + 1

        for j in range(i, left, -1):
            values[j] = values[j - 1]
        values[left] = current


def _merge_collapse(values: list[int], runs: list[tuple[int, int]]) -> None:
    """维护 run 栈不变量，避免后续归并顺序过度失衡。"""

    while len(runs) > 1:
        n = len(runs) - 1

        # 维护 run 栈规模关系，避免形成代价很高的极端归并顺序。
        if n >= 2 and runs[n - 2][1] <= runs[n - 1][1] + runs[n][1]:
            if runs[n - 2][1] < runs[n][1]:
                _merge_at(values, runs, n - 2)
            else:
                _merge_at(values, runs, n - 1)
        elif runs[n - 1][1] <= runs[n][1]:
            _merge_at(values, runs, n - 1)
        else:
            break


def _merge_force_collapse(values: list[int], runs: list[tuple[int, int]]) -> None:
    """输入扫描结束后，强制把剩余 run 合并成一个完整有序区间。"""

    # 输入扫描结束后，将栈上剩余 run 全部合并为一个有序区间。
    while len(runs) > 1:
        n = len(runs) - 2
        if n > 0 and runs[n - 1][1] < runs[n + 1][1]:
            n -= 1
        _merge_at(values, runs, n)


def _merge_at(values: list[int], runs: list[tuple[int, int]], index: int) -> None:
    """稳定合并 runs[index] 和 runs[index + 1] 两个相邻 run。"""

    start_a, length_a = runs[index]
    start_b, length_b = runs[index + 1]
    left = values[start_a : start_a + length_a]
    right = values[start_b : start_b + length_b]

    i = 0
    j = 0
    write = start_a

    while i < length_a and j < length_b:
        # 相等时优先取左侧元素，保持稳定性。
        if left[i] <= right[j]:
            values[write] = left[i]
            i += 1
        else:
            values[write] = right[j]
            j += 1
        write += 1

    while i < length_a:
        values[write] = left[i]
        i += 1
        write += 1

    while j < length_b:
        values[write] = right[j]
        j += 1
        write += 1

    runs[index] = (start_a, length_a + length_b)
    del runs[index + 1]
