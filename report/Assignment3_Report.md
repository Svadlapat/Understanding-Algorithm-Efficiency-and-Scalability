Part 1: Randomized Quicksort Analysis

1. Implementation Overview

Two Quicksort versions were implemented:
randomized_quicksort.py: The pivot is chosen uniformly at random from the subarray arr[low...high]. This pivot is then swapped to the high position before standard partitioning.

deterministic_quicksort.py: The pivot is always the first element of the subarray (arr[low]). This is a classic deterministic approach susceptible to worst-case inputs.

2. Analysis: Average-Case Time Complexity
The average-case time complexity of Randomized Quicksort is O(n\log n).
Reasoning via Indicator Random Variables:
1.Goal: Determine the expected number of comparisons, E[X], performed by the algorithm.

2.Comparison Event: Two elements, z_i (the i-th smallest) and z_j (the j-th smallest, i < j), are compared if and only if one of them is chosen as a pivot before any element between them (i.e., z_i+1,...., z_j-1) is chosen.

3.Probability of Comparison: Consider the set of elements Z_i,j = z_i, z_i+1,...., z_j. Since the pivot is chosen uniformly at random, every element in Z_i,j is equally likely to be the first pivot chosen from this set. 
The size of this set is j - i + 1. Thus, the probability that z_i and z_j are compared is the probability that z_i or z_j is the first pivot chosen from Z_i,j:
P(z_i and z_j are compared) = 2/j - i + 1

4.Expected Comparisons: By summing this probability over all pairs (i, j) and simplifying the resulting harmonic series sum, the total expected number of comparisons is found to be:
$$E[X] = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \frac{2}{j - i + 1} \approx 2n \ln n = \mathbf{O(n \log n)}$$

This analysis shows that randomization, on average, ensures a reasonably balanced partition, guaranteeing the highly efficient O(n \log n) time complexity, independent of the input order.

3.Comparison: Empirical Results and Discussion
The script quicksort_comparison.py measured the runtime for various input distributions and sizes (summarized for $N=10000$):
Input Distribution,Randomized Quicksort (s),Deterministic Quicksort (s),Observed Complexity
Random,0.018203,0.012762,O(nlogn) (Both)
Sorted,0.016247,1.518385,O(nlogn) (Rand) / O(n2) (Det)
Reverse,0.016760,2.998326,O(nlogn) (Rand) / O(n2) (Det)
Repeated,4.347534,1.448969,O(n2) (Rand) / O(n2) (Det)

Discussion:
1.Sorted and Reverse-Sorted Arrays: The deterministic approach (first element as pivot) hit its $\mathbf{O(n^2)}$ worst-case performance, taking significantly longer (up to $\sim 180 \times$ slower for Reverse-sorted arrays at $N=10000$). 
The Randomized Quicksort successfully avoided this worst-case, maintaining its expected $\mathbf{O(n \log n)}$ performance. This confirms the efficacy of randomization in mitigating pathological inputs.
2.Discrepancy (Repeated Elements): For arrays with identical elements, the Randomized Quicksort implementation was significantly slower than the Deterministic version. This is because the specific partition function used (randomized_partition) places all elements less than or equal to the pivot on one side. When all elements are the same, 
this results in an unbalanced partition (one sub-array of size $n-1$, one of size 0), causing the randomized algorithm to degrade to $\mathbf{O(n^2)}$ in this specific edge case. A more sophisticated 3-way partition scheme would resolve this.

Part 2: Hashing with Chaining Analysis:

1.Implementation Overview
The hash_table_chaining.py implements a hash table using a list of lists (chains) for collision resolution. It uses Python's built-in hash(key) % self.capacity as the hash function. 
Crucially, it includes dynamic resizing (_rehash) when the load factor exceeds a threshold (set to 0.75).

2. Analysis: Expected Times and Load Factor
We assume Simple Uniform Hashing (SUH), where each key is equally likely to hash into any of the $m$ slots, independent of other keys. 
The performance is analyzed based on the load factor, $\alpha = n/m$ (number of elements $n$ over capacity $m$).

Operation,Expected Time Complexity (SUH),Impact of α
Search (Unsuccessful),O(1+α),Directly proportional to α. A high α means longer chains to traverse.
Search (Successful),O(1+α),Expected time is O(1) plus approximately half the length of the chain.
Insert,O(1) (Amortized),Time is dominated by hash computation (O(1)) and insertion at the head of the chain (O(1)).
Delete,O(1+α),Requires search time O(1+α) plus removal time O(1).

Key takeaway: When the load factor $\alpha$ is kept constant (i.e., $\alpha = O(1)$), the expected time for all three operations becomes $\mathbf{O(1)}$.

3.Strategies for Maintaining Low Load Factor:

To ensure the $\mathbf{O(1)}$ expected performance, the load factor must be bounded.
Dynamic Resizing (Rehashing): The implemented strategy is to monitor the load factor and, if it exceeds the $\mathbf{0.75}$ threshold, to double the hash table's capacity ($\mathbf{m \to 2m}$).
Effect: Doubling the capacity immediately halves the load factor (e.g., from $0.76$ down to $\sim 0.38$).
Amortization: While the worst-case time for a single insertion that triggers a rehash is $\mathbf{O(n)}$ (to reinsert all $n$ elements), the total cost is amortized over a sequence of insertions. 
Since the capacity only doubles after $\Omega(m)$ insertions, the average cost of an insertion remains $\mathbf{O(1)}$ (amortized time). This ensures long-term scalability and efficiency.

