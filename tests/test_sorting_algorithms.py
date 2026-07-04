"""排序算法单元测试。

测试重点不是证明某个算法的复杂度，而是统一验证项目接口约束：
每个算法都必须返回与 sorted() 一致的结果，并且不能修改传入的原始列表。
"""

import random
import unittest

from lib.registry import iter_algorithms


class SortingAlgorithmTest(unittest.TestCase):
    """覆盖算法注册表和全部排序函数的基础正确性测试。"""

    def test_algorithm_metadata_is_unique(self) -> None:
        """算法 key 必须唯一，避免 CLI 选择和 benchmark 输出混淆。"""

        keys = [spec.key for spec in iter_algorithms()]

        self.assertEqual(len(keys), len(set(keys)))
        self.assertGreaterEqual(len(keys), 15)

    def test_all_algorithms_match_builtin_sorted(self) -> None:
        """所有算法都要在同一批样例上匹配 Python 内置 sorted。"""

        cases = self._build_cases()

        for spec in iter_algorithms():
            with self.subTest(algorithm=spec.key):
                for case in cases:
                    source = case[:]
                    actual = spec.function(source)

                    self.assertEqual(actual, sorted(case))
                    self.assertEqual(source, case)

    def _build_cases(self) -> list[list[int]]:
        """构造固定样例、随机样例和近乎有序样例。"""

        cases = [
            [],
            [1],
            [2, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 3, 3, 3],
            [4, -1, 0, -7, 8, 3, 3, -1],
            [100, -100, 50, -50, 0, 25, -25],
            list(range(64)),
            list(range(64, 0, -1)),
            [0, -1, 1, -1, 0, 1, 999, -999],
        ]

        rng = random.Random(20260517)
        for length in [0, 1, 2, 3, 7, 16, 31, 64, 127]:
            for _ in range(5):
                cases.append([rng.randint(-250, 250) for _ in range(length)])

        for length in [16, 64, 128]:
            values = list(range(length))
            for _ in range(max(1, length // 12)):
                left = rng.randrange(length)
                right = rng.randrange(length)
                values[left], values[right] = values[right], values[left]
            cases.append(values)

        return cases


if __name__ == "__main__":
    unittest.main()
