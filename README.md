# Advanced Sorting Algorithms

Advanced Sorting Algorithms is a Python project for implementing, validating, and analyzing sorting algorithms. It brings common sorts, divide-and-conquer sorts, distribution-based sorts, and hybrid sorts into one consistent interface. The project provides reproducible correctness checks and local benchmark tooling, making it easier to compare how algorithms behave under different data distributions, input sizes, and stability requirements.

## Project Goals

- Implement a broad set of sorting algorithms with consistent input and output conventions.
- Record each algorithm's stability, complexity, space cost, applicable scenarios, and input constraints.
- Validate results against `sorted()` using deterministic and randomized samples.
- Provide configurable benchmarks that use fixed random seeds to reproduce timings across data distributions.
- Keep the project structure clear so algorithms, tests, and experiment dimensions can be extended easily.

## Core Features

- Sorting algorithm library: all algorithms live in `lib/`; each function accepts `list[int]`, returns a new sorted list, and does not mutate the input array.
- Algorithm registry: `lib/registry.py` centrally manages algorithm functions, complexity metadata, stability, and usage notes.
- Command-line entry point: `main.py` can list algorithms, run correctness verification, and execute benchmarks.
- Unit tests: `tests/` covers empty arrays, duplicate values, negative numbers, reversed input, nearly sorted input, and random input.
- Benchmarks: `benchmarks/benchmark.py` supports multiple input sizes, data distributions, repeated runs, and CSV/JSON output.

## Implemented Algorithms

| Algorithm | Type | Average Time Complexity | Worst Time Complexity | Space Complexity | Stable |
| --- | --- | --- | --- | --- | --- |
| Bubble Sort | exchange | O(n^2) | O(n^2) | O(1) | Yes |
| Cocktail Shaker Sort | exchange | O(n^2) | O(n^2) | O(1) | Yes |
| Comb Sort | exchange | O(n^2 / 2^p) | O(n^2) | O(1) | No |
| Selection Sort | selection | O(n^2) | O(n^2) | O(1) | No |
| Insertion Sort | insertion | O(n^2) | O(n^2) | O(1) | Yes |
| Shell Sort | insertion | Depends on gap sequence | O(n^2) | O(1) | No |
| Merge Sort | merge | O(n log n) | O(n log n) | O(n) | Yes |
| Tim Sort | hybrid | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | partition | O(n log n) | O(n^2) | O(log n) | No |
| Stable Quick Sort | partition | O(n log n) | O(n^2) | O(n) | Yes |
| Three-way Quick Sort | partition | O(n log n) | O(n^2) | O(log n) | No |
| Dual-pivot Quick Sort | partition | O(n log n) | O(n^2) | O(log n) | No |
| Intro Sort | hybrid | O(n log n) | O(n log n) | O(log n) | No |
| Heap Sort | selection | O(n log n) | O(n log n) | O(1) | No |
| Tree Sort | tree | O(n log n) | O(n^2) | O(n) | No |
| Counting Sort | distribution | O(n + k) | O(n + k) | O(k) | Yes |
| Radix Sort | distribution | O(dn) | O(dn) | O(n) | Yes |
| Bucket Sort | distribution | O(n + k) | O(n^2) | O(n + k) | Yes |

## Tech Stack

- Python 3.10+
- Standard library `argparse`, `random`, `time`, `statistics`, `csv`, `json`
- Standard library `unittest`
- No third-party dependencies

## Project Structure

```text
advanced-sorting-algorithms/
├── README.md
├── .gitignore
├── main.py
├── benchmarks/
│   ├── __init__.py
│   └── benchmark.py
├── lib/
│   ├── __init__.py
│   ├── registry.py
│   ├── bubble_sort.py
│   ├── bucket_sort.py
│   ├── cocktail_sort.py
│   ├── comb_sort.py
│   ├── counting_sort.py
│   ├── dual_pivot_quick_sort.py
│   ├── heap_sort.py
│   ├── insertion_sort.py
│   ├── intro_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── radix_sort.py
│   ├── selection_sort.py
│   ├── shell_sort.py
│   ├── stable_quick_sort.py
│   ├── three_way_quick_sort.py
│   ├── tim_sort.py
│   └── tree_sort.py
└── tests/
    └── test_sorting_algorithms.py
```

## Usage

List all algorithms and metadata:

```bash
python3 main.py list
```

Run correctness verification:

```bash
python3 main.py verify
```

Verify only selected algorithms:

```bash
python3 main.py verify --algorithms intro_sort,tim_sort,three_way_quick_sort
```

Run a local benchmark:

```bash
python3 main.py benchmark --sizes 32,128,512 --repeat 3
```

Write benchmark results to a file:

```bash
python3 main.py benchmark --sizes 64,256,1024 --output benchmarks/results/latest.csv
```

Run unit tests:

```bash
python3 -B -m unittest discover -s tests
```

## Correctness Verification

The verification logic covers:

- empty arrays and single-element arrays
- sorted arrays and reversed arrays
- duplicate elements
- mixed negative numbers, zero, and positive numbers
- integers with a large value range
- random arrays generated with fixed random seeds
- nearly sorted arrays
- the interface requirement that the input array is not mutated

Every algorithm's output is compared with Python's built-in `sorted()` result.

## Benchmark Notes

Benchmarks support the following data distributions:

- `random`: random integer distribution
- `sorted`: fully sorted input
- `reversed`: fully reversed input
- `duplicates`: dense duplicate values
- `nearly_sorted`: nearly sorted arrays with local perturbations

By default, benchmarks do not save results and only print a table in the terminal. When experiment data needs to be preserved, use `--output` to write `.csv` or `.json` files. The repository does not include fixed performance conclusions, because runtimes from different machines and Python interpreter versions should not be mixed together.

## Current Progress

- 18 sorting algorithms are implemented.
- A unified algorithm registry is complete.
- CLI entry point, correctness verification, and benchmark tooling are complete.
- `unittest` test cases are complete.
- README and `.gitignore` have been added.

## Roadmap

- Add an external sorting example using chunks, temporary files, and multiway merge for memory-constrained scenarios.
- Add more detailed benchmark reports, including comparison counts, swap counts, and peak memory usage.
- Add an object-sorting version for stability validation, so records with equal values but different original positions can be distinguished.
- Add visualization output to generate charts for algorithm behavior across input sizes and distributions.
