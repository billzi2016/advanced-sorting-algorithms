from __future__ import annotations


class _Node:
    __slots__ = ("value", "count", "left", "right")

    def __init__(self, value: int) -> None:
        self.value = value
        self.count = 1
        self.left: _Node | None = None
        self.right: _Node | None = None


def tree_sort(values: list[int]) -> list[int]:
    if not values:
        return []

    # 未使用自平衡树，最坏情况下会退化；这里重点展示 BST 排序思路。
    root = _Node(values[0])
    for value in values[1:]:
        _insert(root, value)

    result: list[int] = []
    _in_order(root, result)
    return result


def _insert(root: _Node, value: int) -> None:
    current = root

    while True:
        if value < current.value:
            if current.left is None:
                current.left = _Node(value)
                return
            current = current.left
        elif value > current.value:
            if current.right is None:
                current.right = _Node(value)
                return
            current = current.right
        else:
            # 重复值用计数压缩，避免树上创建大量相同节点。
            current.count += 1
            return


def _in_order(node: _Node | None, result: list[int]) -> None:
    if node is None:
        return

    # 二叉搜索树的中序遍历天然按升序输出。
    _in_order(node.left, result)
    result.extend([node.value] * node.count)
    _in_order(node.right, result)
