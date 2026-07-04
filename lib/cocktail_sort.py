"""鸡尾酒排序。

鸡尾酒排序是双向冒泡排序：一次从左到右把大值推到右端，
再从右到左把小值推到左端。它对“元素距离正确位置不远”的局部乱序输入
比普通单向冒泡更敏感。
"""


def cocktail_sort(values: list[int]) -> list[int]:
    """使用双向冒泡策略返回升序副本。"""

    # 复制输入，保证函数满足项目约定：排序过程不修改原数组。
    result = values[:]
    if len(result) <= 1:
        return result

    start = 0
    end = len(result) - 1
    swapped = True

    while swapped:
        swapped = False

        # 正向扫描：把当前未排序区间的最大值推到右边界。
        for i in range(start, end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # 反向扫描：把当前未排序区间的最小值推到左边界。
        for i in range(end, start, -1):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swapped = True

        start += 1

    return result
