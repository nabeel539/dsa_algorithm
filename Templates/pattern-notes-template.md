# [Pattern Name]

## 1. Pattern Overview
A concise explanation of the pattern, what it represents, and why it is an essential algorithmic tool.

---

## 2. What Problem Does This Pattern Solve?
- The fundamental inefficiency or challenge this pattern tackles.
- Common computational bottlenecks reduced (e.g., reducing $O(N^2)$ brute-force nested loops to $O(N)$ or $O(N \log N)$).

---

## 3. When Should I Use This Pattern?
- Input characteristics (e.g., sorted arrays, contiguous subarrays, tree structures).
- Output requirements (e.g., finding optimal pairs, maximum sum window, min path).
- Specific problem constraints (e.g., in-place $O(1)$ extra space requirements).

---

## 4. How to Identify the Pattern from a Question
### Keyword Clues & Signals
- Look for keywords: `contiguous`, `triplet sum`, `sorted order`, `k elements`, `shortest substring`.
- Problem statements asking for min/max within constraints or finding target combinations.

### Problem Constraints Clues
- $N \le 10^5 \implies O(N)$ or $O(N \log N)$ expected.
- In-place modification requested $\implies$ pointers or swaps.

---

## 5. Core Intuition
The mental model or visualization:
- How does the approach eliminate redundant calculations?
- What invariants are maintained at every step?

---

## 6. General Algorithm & Reusable Templates

### General Python Template
```python
def pattern_template(data):
    """
    Template explanation and generic skeleton.
    """
    # 1. Initialize state / pointers
    left, right = 0, len(data) - 1
    result = []

    # 2. Iterate while condition holds
    while left < right:
        # Evaluate condition
        current = data[left] + data[right]
        if current == target:
            result.append((data[left], data[right]))
            left += 1
            right -= 1
        elif current < target:
            left += 1
        else:
            right -= 1

    return result
```

---

## 7. Step-by-Step Algorithm
1. **Pre-processing / Sorting**: Clarify if input needs sorting or structure transformation.
2. **Initialization**: Define initial pointer positions, variables, or data structures.
3. **Loop Condition**: State clearly when iteration stops.
4. **Transition / Invariant Maintenance**: How pointers or states move based on decisions.
5. **Termination & Output**: Final extraction or calculation of the answer.

---

## 8. Time and Space Complexity
- **Time Complexity:**
  - Best Case: $O(...)$
  - Average Case: $O(...)$
  - Worst Case: $O(...)$
- **Space Complexity:**
  - Extra Auxiliary Space: $O(...)$

---

## 9. Common Edge Cases
- Empty collection or single element input (`len(nums) == 0` or `len(nums) == 1`).
- Duplicate elements or identical values across the dataset.
- Negative numbers, zeros, or extreme value limits (`-2^31` to `2^31 - 1`).
- All elements satisfying or no elements satisfying the condition.

---

## 10. Common Mistakes & Debugging Notes
- Off-by-one errors in while loops (`left < right` vs `left <= right`).
- Forgetting to handle duplicates after matching elements.
- Modifying pointers inside conditional branches incorrectly leading to infinite loops.
- Overlooking indexing boundaries.

---

## 11. Brute Force vs Optimized Approach

| Aspect | Brute Force Approach | Optimized (Pattern) Approach |
| :--- | :--- | :--- |
| **Strategy** | Exhaustive search across all combinations | Pruning search space using invariants |
| **Time Complexity** | $O(N^2)$ or $O(N^3)$ | $O(N)$ or $O(N \log N)$ |
| **Space Complexity** | $O(1)$ or $O(N)$ | $O(1)$ auxiliary space |
| **Trade-offs** | Simple to implement, TLE on large $N$ | Requires sorted input or pointer tracking |

---

## 12. Comparison with Related Patterns

| Pattern | Similarities | Differences | When to choose this over others |
| :--- | :--- | :--- | :--- |
| **Alternative Pattern A** | Both work on arrays | Handles non-contiguous vs contiguous elements | Choose when elements can be reordered |
| **Alternative Pattern B** | Uses two indices | Moves in same direction vs opposite directions | Choose when tracking dynamic subsegments |

---

## 13. Problems to Solve

| # | Problem | Difficulty | Status | File Link |
| :-: | :--- | :-: | :-: | :--- |
| 1 | Problem Title 1 | Easy | Not Started | [problem-1.md](problems/01-problem.md) |
| 2 | Problem Title 2 | Medium | Not Started | [problem-2.md](problems/02-problem.md) |
| 3 | Problem Title 3 | Hard | Not Started | [problem-3.md](problems/03-problem.md) |

---

## 14. Revision Checklist
- [ ] Can explain core intuition verbally in under 90 seconds without looking at code.
- [ ] Can write the general template from memory on a blank whiteboard / editor.
- [ ] Understand key edge cases and how the template handles them.
- [ ] Solved at least 3 representative problems independently.

---

## 15. Links to Individual Problem Files
- [Problem 1 Notes](problems/01-problem.md)
- [Problem 2 Notes](problems/02-problem.md)
