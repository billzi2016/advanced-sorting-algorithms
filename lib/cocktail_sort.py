def cocktail_sort(values: list[int]) -> list[int]:
    result = values[:]
    if len(result) <= 1:
        return result

    start = 0
    end = len(result) - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start, -1):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swapped = True

        start += 1

    return result
