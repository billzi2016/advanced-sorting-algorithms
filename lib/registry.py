"""排序算法注册表。

这个模块把算法函数和它们的元数据集中放在一起，避免 README、CLI、
测试和 benchmark 各自维护一份算法清单。新增算法时，通常只需要实现函数，
再在 ALGORITHMS 中补一条 AlgorithmSpec。
"""

from dataclasses import dataclass
from typing import Callable

from lib.bubble_sort import bubble_sort
from lib.bucket_sort import bucket_sort
from lib.cocktail_sort import cocktail_sort
from lib.comb_sort import comb_sort
from lib.counting_sort import counting_sort
from lib.dual_pivot_quick_sort import dual_pivot_quick_sort
from lib.heap_sort import heap_sort
from lib.insertion_sort import insertion_sort
from lib.intro_sort import intro_sort
from lib.merge_sort import merge_sort
from lib.quick_sort import quick_sort
from lib.radix_sort import radix_sort
from lib.selection_sort import selection_sort
from lib.shell_sort import shell_sort
from lib.stable_quick_sort import stable_quick_sort
from lib.three_way_quick_sort import three_way_quick_sort
from lib.tim_sort import tim_sort
from lib.tree_sort import tree_sort

SortFunction = Callable[[list[int]], list[int]]


@dataclass(frozen=True)
class AlgorithmSpec:
    """单个排序算法的注册信息。

    function 必须遵守项目统一接口：接收 list[int]，返回新的升序 list[int]，
    不修改调用方传入的列表。复杂度和适用说明用于 CLI 展示和 README 对齐。
    """

    # 注册表元数据用于 CLI、测试、benchmark 和文档保持同一套算法清单。
    key: str
    display_name: str
    function: SortFunction
    family: str
    stable: bool
    mutates_input: bool
    best_time: str
    average_time: str
    worst_time: str
    space: str
    constraints: str
    description: str


ALGORITHMS: tuple[AlgorithmSpec, ...] = (
    AlgorithmSpec(
        key="bubble_sort",
        display_name="Bubble Sort",
        function=bubble_sort,
        family="exchange",
        stable=True,
        mutates_input=False,
        best_time="O(n)",
        average_time="O(n^2)",
        worst_time="O(n^2)",
        space="O(1)",
        constraints="通用整数数组",
        description="带提前终止优化的相邻交换排序，适合作为稳定交换排序基线。",
    ),
    AlgorithmSpec(
        key="cocktail_sort",
        display_name="Cocktail Shaker Sort",
        function=cocktail_sort,
        family="exchange",
        stable=True,
        mutates_input=False,
        best_time="O(n)",
        average_time="O(n^2)",
        worst_time="O(n^2)",
        space="O(1)",
        constraints="通用整数数组",
        description="双向冒泡排序，对局部逆序分布比单向冒泡更敏感。",
    ),
    AlgorithmSpec(
        key="comb_sort",
        display_name="Comb Sort",
        function=comb_sort,
        family="exchange",
        stable=False,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n^2 / 2^p)",
        worst_time="O(n^2)",
        space="O(1)",
        constraints="通用整数数组",
        description="使用递减 gap 消除远距离逆序，是冒泡排序的一种工程改进。",
    ),
    AlgorithmSpec(
        key="selection_sort",
        display_name="Selection Sort",
        function=selection_sort,
        family="selection",
        stable=False,
        mutates_input=False,
        best_time="O(n^2)",
        average_time="O(n^2)",
        worst_time="O(n^2)",
        space="O(1)",
        constraints="通用整数数组",
        description="每轮选择未排序区间最小值，交换次数少但比较次数固定。",
    ),
    AlgorithmSpec(
        key="insertion_sort",
        display_name="Insertion Sort",
        function=insertion_sort,
        family="insertion",
        stable=True,
        mutates_input=False,
        best_time="O(n)",
        average_time="O(n^2)",
        worst_time="O(n^2)",
        space="O(1)",
        constraints="通用整数数组",
        description="适合小规模和近乎有序输入，也是多种混合排序的基础组件。",
    ),
    AlgorithmSpec(
        key="shell_sort",
        display_name="Shell Sort",
        function=shell_sort,
        family="insertion",
        stable=False,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="依赖 gap 序列",
        worst_time="O(n^2)",
        space="O(1)",
        constraints="通用整数数组",
        description="按 gap 分组执行插入排序，降低远距离元素移动成本。",
    ),
    AlgorithmSpec(
        key="merge_sort",
        display_name="Merge Sort",
        function=merge_sort,
        family="merge",
        stable=True,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n log n)",
        worst_time="O(n log n)",
        space="O(n)",
        constraints="通用整数数组",
        description="稳定分治排序，时间复杂度稳定，适合链式结构和外部排序思想扩展。",
    ),
    AlgorithmSpec(
        key="tim_sort",
        display_name="Tim Sort",
        function=tim_sort,
        family="hybrid",
        stable=True,
        mutates_input=False,
        best_time="O(n)",
        average_time="O(n log n)",
        worst_time="O(n log n)",
        space="O(n)",
        constraints="通用整数数组",
        description="基于自然 run、二分插入和稳定归并的简化 TimSort 实现。",
    ),
    AlgorithmSpec(
        key="quick_sort",
        display_name="Quick Sort",
        function=quick_sort,
        family="partition",
        stable=False,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n log n)",
        worst_time="O(n^2)",
        space="O(log n)",
        constraints="通用整数数组",
        description="中位位置选基准的原地分区快速排序实现。",
    ),
    AlgorithmSpec(
        key="stable_quick_sort",
        display_name="Stable Quick Sort",
        function=stable_quick_sort,
        family="partition",
        stable=True,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n log n)",
        worst_time="O(n^2)",
        space="O(n)",
        constraints="通用整数数组",
        description="使用 left/mid/right 分区保持相等元素相对顺序的稳定快速排序。",
    ),
    AlgorithmSpec(
        key="three_way_quick_sort",
        display_name="Three-way Quick Sort",
        function=three_way_quick_sort,
        family="partition",
        stable=False,
        mutates_input=False,
        best_time="O(n)",
        average_time="O(n log n)",
        worst_time="O(n^2)",
        space="O(log n)",
        constraints="通用整数数组，重复值较多时表现更好",
        description="Dijkstra 三路分区，把小于、等于、大于基准的元素一次划分完成。",
    ),
    AlgorithmSpec(
        key="dual_pivot_quick_sort",
        display_name="Dual-pivot Quick Sort",
        function=dual_pivot_quick_sort,
        family="partition",
        stable=False,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n log n)",
        worst_time="O(n^2)",
        space="O(log n)",
        constraints="通用整数数组",
        description="使用两个基准将数组划分为三段，体现现代库排序中的分区思路。",
    ),
    AlgorithmSpec(
        key="intro_sort",
        display_name="Intro Sort",
        function=intro_sort,
        family="hybrid",
        stable=False,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n log n)",
        worst_time="O(n log n)",
        space="O(log n)",
        constraints="通用整数数组",
        description="快速排序、堆排序和插入排序的混合策略，避免快速排序最坏退化。",
    ),
    AlgorithmSpec(
        key="heap_sort",
        display_name="Heap Sort",
        function=heap_sort,
        family="selection",
        stable=False,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n log n)",
        worst_time="O(n log n)",
        space="O(1)",
        constraints="通用整数数组",
        description="基于最大堆反复选择当前最大值，空间占用稳定。",
    ),
    AlgorithmSpec(
        key="tree_sort",
        display_name="Tree Sort",
        function=tree_sort,
        family="tree",
        stable=False,
        mutates_input=False,
        best_time="O(n log n)",
        average_time="O(n log n)",
        worst_time="O(n^2)",
        space="O(n)",
        constraints="通用整数数组；未做自平衡",
        description="构建二叉搜索树并中序遍历，展示树结构与排序的关系。",
    ),
    AlgorithmSpec(
        key="counting_sort",
        display_name="Counting Sort",
        function=counting_sort,
        family="distribution",
        stable=True,
        mutates_input=False,
        best_time="O(n + k)",
        average_time="O(n + k)",
        worst_time="O(n + k)",
        space="O(k)",
        constraints="整数值域不宜过大",
        description="按值域计数并展开结果，当前实现支持负数偏移。",
    ),
    AlgorithmSpec(
        key="radix_sort",
        display_name="Radix Sort",
        function=radix_sort,
        family="distribution",
        stable=True,
        mutates_input=False,
        best_time="O(dn)",
        average_time="O(dn)",
        worst_time="O(dn)",
        space="O(n)",
        constraints="整数输入；当前实现支持负数拆分",
        description="按十进制位执行稳定计数排序，适合整数键排序。",
    ),
    AlgorithmSpec(
        key="bucket_sort",
        display_name="Bucket Sort",
        function=bucket_sort,
        family="distribution",
        stable=True,
        mutates_input=False,
        best_time="O(n + k)",
        average_time="O(n + k)",
        worst_time="O(n^2)",
        space="O(n + k)",
        constraints="输入分布越均匀越合适",
        description="按数值区间映射到桶内排序，再按桶顺序合并。",
    ),
)


def iter_algorithms() -> tuple[AlgorithmSpec, ...]:
    """返回全部算法注册信息。"""

    return ALGORITHMS


def get_algorithm(key: str) -> AlgorithmSpec:
    """按 key 查找算法注册信息；不存在时抛出 KeyError。"""

    for spec in ALGORITHMS:
        if spec.key == key:
            return spec
    raise KeyError(f"unknown algorithm: {key}")
