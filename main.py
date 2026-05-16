from lib.bubble_sort import bubble_sort
from lib.bucket_sort import bucket_sort
from lib.counting_sort import counting_sort
from lib.heap_sort import heap_sort
from lib.insertion_sort import insertion_sort
from lib.merge_sort import merge_sort
from lib.quick_sort import quick_sort
from lib.radix_sort import radix_sort
from lib.selection_sort import selection_sort
from lib.shell_sort import shell_sort
from lib.stable_quick_sort import stable_quick_sort


def run_correctness_test(name, sort_func, test_cases):
    for case in test_cases:
        actual = sort_func(case)
        expected = sorted(case)

        if actual != expected:
            print(f"[FAIL] {name}")
            print(f"input:    {case}")
            print(f"expected: {expected}")
            print(f"actual:   {actual}")
            return False

    print(f"[PASS] {name}")
    return True


def main():
    test_cases = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 3, 3],
        [4, -1, 0, -7, 8, 3, 3, -1],
        [10, 9, 8, 1, 2, 7, 6, 3, 5, 4],
        [100, -100, 50, -50, 0, 25, -25],
        [42, 17, 8, 99, 23, 4, 16, 15, 15, 0, -3, -100, 2048],
    ]

    algorithms = [
        ("bubble_sort", bubble_sort),
        ("selection_sort", selection_sort),
        ("insertion_sort", insertion_sort),
        ("shell_sort", shell_sort),
        ("merge_sort", merge_sort),
        ("quick_sort", quick_sort),
        ("stable_quick_sort", stable_quick_sort),
        ("heap_sort", heap_sort),
        ("counting_sort", counting_sort),
        ("radix_sort", radix_sort),
        ("bucket_sort", bucket_sort),
    ]

    for name, sort_func in algorithms:
        if not run_correctness_test(name, sort_func, test_cases):
            raise SystemExit(1)

    print("All sorting algorithms passed correctness tests.")


if __name__ == "__main__":
    main()
