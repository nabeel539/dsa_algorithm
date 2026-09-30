# Complexity Analysis for DSA & Coding Interviews

Understanding time and space complexity is the first thing interviewers evaluate. A candidate who writes working code without knowing its complexity will rarely pass top-tier rounds.

---

## 1. Asymptotic Notations

- **Big-O ($O$): Upper Bound.** Describes the worst-case scenario. Guarantees that execution time or space will not exceed this rate as $N \to \infty$. This is standard for technical interviews.
- **Big-Omega ($\Omega$): Lower Bound.** Describes the best-case execution rate.
- **Big-Theta ($\Theta$): Tight Bound.** Describes algorithms where best and worst cases scale at the exact same asymptotic rate (e.g., merge sort is $\Theta(N \log N)$).

---

## 2. Common Time Complexities (Fastest to Slowest)

| Notation | Name | Typical Example | Input Size Limit ($N$) for 1 sec execution |
| :---: | :--- | :--- | :---: |
| $O(1)$ | Constant | Accessing array element by index, hash map lookup | Any size |
| $O(\log N)$ | Logarithmic | Binary Search, operations on balanced BSTs | $N \le 10^9$ |
| $O(N)$ | Linear | Single pass over array, linear search | $N \le 10^7$ |
| $O(N \log N)$ | Linearithmic | Merge Sort, Timsort (`sorted()`), Heap Sort | $N \le 10^6$ |
| $O(N^2)$ | Quadratic | Nested loops, bubble sort, naive all-pairs comparisons | $N \le 5,000$ |
| $O(N^3)$ | Cubic | Naive 3Sum, matrix multiplication | $N \le 500$ |
| $O(2^N)$ | Exponential | Subsets generation, recursive Fibonacci | $N \le 20$ |
| $O(N!)$ | Factorial | Generating all permutations, Traveling Salesperson (brute-force) | $N \le 10$ |

---

## 3. Estimating Expected Complexity from Constraints

Use this rule of thumb during interviews to deduce the target algorithm before writing code:

- **$N \le 10$:** $O(N!)$ or $O(2^N \times N)$ — Backtracking, brute-force search.
- **$N \le 20$:** $O(2^N)$ — Bitmask Dynamic Programming, recursion with memoization.
- **$N \le 100$:** $O(N^4)$ or $O(N^3)$ — 2D DP, Floyd-Warshall, 3 nested loops.
- **$N \le 1,000$:** $O(N^2)$ — 2 nested loops, dynamic programming, 2-pointer nested checks.
- **$N \le 10^5$:** $O(N \log N)$ or $O(N)$ — Sorting, heaps, binary search, two pointers, sliding window.
- **$N \le 10^6$:** $O(N)$ — Single pass linear scan, prefix sums, hash maps.
- **$N \ge 10^9$:** $O(\log N)$ or $O(1)$ — Binary search on answer, mathematical formulas, bit operations.

---

## 4. Space Complexity Guidelines

Space complexity evaluates **auxiliary (extra) memory** allocated by the algorithm relative to input size:

1. **In-place algorithms:** $O(1)$ auxiliary space. Do not count input or output space if specified by the question.
2. **Recursion call stack:** Each call frame occupies stack memory. If recursion depth reaches $K$, auxiliary space is $O(K)$.
3. **Data structures:** Hash maps, sets, queues, and heaps storing elements proportionally scale to $O(N)$ auxiliary space.

---

## 5. Analyzing Amortized Complexity

Some operations occasionally perform expensive operations, but the average cost per operation over a sequence of $N$ operations is small:

- **Python `list.append()`:** When the underlying dynamic array capacity is exceeded, Python allocates a new buffer and copies elements ($O(N)$ worst-case). However, array resizing happens geometrically, meaning $N$ appends take $O(N)$ total time $\implies$ **Amortized $O(1)$** per append.
- **Hash Table Resizing:** Similar to dynamic arrays, hash table re-hashing occurs occasionally, but lookups and insertions remain **Amortized $O(1)$**.
