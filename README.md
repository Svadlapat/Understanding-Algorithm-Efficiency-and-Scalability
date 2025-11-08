# Understanding-Algorithm-Efficiency-and-Scalability
# Understanding Algorithm Efficiency and Scalability

This repository contains the implementation and analysis for Assignment 3, which focuses on the efficiency and scalability of **Randomized Quicksort** and **Hashing with Chaining**.

## Project Structure

* `randomized_quicksort.py`: Implementation of Quicksort with a randomly chosen pivot.
* `deterministic_quicksort.py`: Implementation of Quicksort with the first element as the pivot (a common deterministic approach).
* `quicksort_comparison.py`: Script for empirically comparing the running times of Randomized and Deterministic Quicksort across various input distributions and sizes.
* `hash_table_chaining.py`: Implementation of a Hash Table using the chaining method for collision resolution, including dynamic resizing.


## How to Run the Code

### Prerequisites

* Python 3.x installed

### 1. Randomized Quicksort and Deterministic Quicksort

To see the basic sorting functionality:

```bash
# Run the randomized version
python randomized_quicksort.py

# Run the deterministic version
python deterministic_quicksort.py

# Run the quicksort version:
python quicksort_comparison.py

# Run the hash table chaining
python hash_table_chaining.py