import time, random
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort
import sys
sys.setrecursionlimit(1000000)

def run_test(arr):
    arr1 = arr.copy()
    start = time.time()
    randomized_quicksort(arr1, 0, len(arr1)-1)
    rand_time = time.time() - start

    arr2 = arr.copy()
    start = time.time()
    deterministic_quicksort(arr2, 0, len(arr2)-1)
    det_time = time.time() - start

    return rand_time, det_time

def generate_arrays(n):
    return [
        ("Random", [random.randint(1, n) for _ in range(n)]),
        ("Sorted", list(range(n))),
        ("Reverse", list(range(n, 0, -1))),
        ("Repeated", [5] * n)
    ]

if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    for n in sizes:
        print(f"\n--- Array size: {n} ---")
        for label, arr in generate_arrays(n):
            rand_t, det_t = run_test(arr)
            print(f"{label:10} | Randomized: {rand_t:.6f}s | Deterministic: {det_t:.6f}s")
