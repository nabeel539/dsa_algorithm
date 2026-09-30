# Recursion Basics & Call Stack Mechanics

Recursion is the engine behind Tree traversals, Graph DFS, Backtracking, and Divide-and-Conquer algorithms.

---

## 1. Anatomy of a Recursive Function

Every valid recursive function must have two key components:
1. **Base Case(s):** The stopping condition where the function returns a value directly without making further recursive calls.
2. **Recursive Step / Transition:** Breaking down the input into smaller subproblems and moving closer towards the base case.

```python
def factorial(n: int) -> int:
    # 1. Base Case: Stops the recursion
    if n <= 1:
        return 1
    
    # 2. Recursive Step: Moves n closer to base case
    return n * factorial(n - 1)
```

---

## 2. The Call Stack Mechanics

When a function calls itself, Python creates a new **stack frame** on the execution call stack containing:
- Local variables
- Parameter arguments
- Return address

```text
factorial(3)
  ├── pushes frame factorial(3) to stack
  ├── calls factorial(2)
        ├── pushes frame factorial(2) to stack
        ├── calls factorial(1)
              ├── pushes frame factorial(1) to stack
              └── returns 1 (pops frame)
        └── computes 2 * 1 = 2 (pops frame)
  └── computes 3 * 2 = 6 (pops frame)
```

### Recursion Depth & Stack Overflow
In Python, default recursion limit is typically 1,000 frames:
```python
import sys
# Check limit
print(sys.getrecursionlimit())

# Increase limit if necessary (use cautiously)
sys.setrecursionlimit(20000)
```
> **Warning:** Exceeding stack depth causes `RecursionError: maximum recursion depth exceeded`. If an algorithm has $O(N)$ depth on $N = 10^5$, convert the solution to an iterative approach using an explicit stack or queue.

---

## 3. Recursion Trees & Complexity

Visualizing recursive branching helps compute time and space complexity.

### Example: Fibonacci (Naive)
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

```text
                  fib(4)
               /          \
          fib(3)          fib(2)
          /    \          /    \
      fib(2)  fib(1)   fib(1)  fib(0)
      /    \
   fib(1) fib(0)
```

- **Height of tree:** $N$
- **Number of nodes:** $2^0 + 2^1 + 2^2 + \dots + 2^N \approx 2^{N+1} - 1 \implies O(2^N)$ Time.
- **Space complexity:** Maximum depth of call stack is $O(N)$.
