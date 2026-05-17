def comb_sort(values: list[int]) -> list[int]:
    result = values[:]
    gap = len(result)
    shrink = 1.3
    sorted_pass = False

    while not sorted_pass:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_pass = True

        for i in range(0, len(result) - gap):
            if result[i] > result[i + gap]:
                result[i], result[i + gap] = result[i + gap], result[i]
                sorted_pass = False

    return result
