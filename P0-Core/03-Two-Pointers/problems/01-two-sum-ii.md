# Two Sum II — Input Array Is Sorted

## Problem Details

* **Platform:** LeetCode (Problem #167)
* **Problem Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
* **Difficulty:** Medium
* **Priority:** P0
* **Pattern:** Two Pointers (Opposite-Direction Convergence)
* **Related Patterns:** Hashing, Binary Search
* **Status:** Not Started
* **Last Revised:** 

---

## 1. Problem Statement

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice. Your solution must use only constant extra space.

---

## 2. Examples

### Example 1
```text
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

### Example 2
```text
Input: numbers = [2, 3, 4], target = 6
Output: [1, 3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

### Example 3
```text
Input: numbers = [-1, 0], target = -1
Output: [1, 2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

---

## 3. Pattern Recognition

* **What clues indicate this pattern?**
  - The input array is already **sorted in non-decreasing order**.
  - We need to find a pair of elements that sum to a specific target value.
  - The problem strictly mandates **$O(1)$ constant extra space**, ruling out a standard hash map approach ($O(N)$ space).
* **Why is this pattern suitable?**
  - Because the array is sorted, the sum of numbers at opposite ends (`left` and `right`) provides a directional guide:
    - If the current sum is smaller than the target, the only way to increase the sum is to increment `left`.
    - If the current sum is greater than the target, the only way to decrease the sum is to decrement `right`.

---

## 4. Brute Force Approach

* **Intuition:**
  - Check every possible pair $(i, j)$ where $i < j$ with two nested loops and compute their sum.
* **Algorithm:**
  1. Outer loop from $i = 0$ to $n - 2$.
  2. Inner loop from $j = i + 1$ to $n - 1$.
  3. If `numbers[i] + numbers[j] == target`, return `[i + 1, j + 1]`.
* **Python Code:**
```python
def two_sum_brute(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []
```
* **Time Complexity:** $O(N^2)$
* **Space Complexity:** $O(1)$
* **Limitations:**
  - On inputs where $N = 3 \times 10^4$, $N^2 \approx 9 \times 10^8$ operations, resulting in Time Limit Exceeded (TLE).

---

## 5. Optimized Approach

* **Intuition:**
  - Exploit the sorted property with two pointers converging from both boundaries.
* **Step-by-step Algorithm:**
  1. Initialize `left = 0` and `right = len(numbers) - 1`.
  2. While `left < right`:
     - Calculate `current_sum = numbers[left] + numbers[right]`.
     - If `current_sum == target`, return `[left + 1, right + 1]` (converting to 1-indexed).
     - If `current_sum < target`, increment `left`.
     - If `current_sum > target`, decrement `right`.
* **Python Code:**
  - See full implementation in [01-two-sum-ii.py](01-two-sum-ii.py).
* **Time Complexity:** $O(N)$ — Each element is examined at most once as pointers converge.
* **Space Complexity:** $O(1)$ — Only two integer pointers are used.

---

## 6. Dry Run

*Input:* `numbers = [2, 7, 11, 15]`, `target = 9`

| Step | `left` (idx, val) | `right` (idx, val) | Sum | Comparison with Target (9) | Action |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 (val: 2) | 3 (val: 15) | 17 | $17 > 9$ | `right -= 1` |
| 2 | 0 (val: 2) | 2 (val: 11) | 13 | $13 > 9$ | `right -= 1` |
| 3 | 0 (val: 2) | 1 (val: 7) | 9 | $9 == 9$ | Target matched! Return `[0+1, 1+1] = [1, 2]` |

---

## 7. Edge Cases

| Edge Case Scenario | Test Input | Expected Output | Outcome / Verified |
| :--- | :--- | :--- | :---: |
| Minimum length array ($N=2$) | `numbers = [1, 2], target = 3` | `[1, 2]` | [ ] |
| Negative numbers included | `numbers = [-5, -3, 0, 2], target = -3` | `[2, 3]` | [ ] |
| Target with identical values | `numbers = [0, 0, 3, 4], target = 0` | `[1, 2]` | [ ] |
| Elements at extreme ends | `numbers = [1, 3, 5, 9], target = 10` | `[1, 4]` | [ ] |

---

## 8. Mistakes I Made

*(To be filled during active practice: record off-by-one errors, indexing mistakes, etc.)*

---

## 9. What I Learned

*(To be filled in your own words after solving)*

---

## 10. Interview Explanation

> "Since the input array is already sorted and we must find two numbers that sum to the target with $O(1)$ extra memory, we can use two converging pointers. We place one pointer at the start and one at the end. At each step, we check the sum. If the sum is smaller than the target, we increment the left pointer to increase the sum; if greater, we decrement the right pointer. This eliminates one element at each step, achieving $O(N)$ time complexity and $O(1)$ space complexity."

---

## 11. Revision

- [ ] Solve without looking at notes
- [ ] Explain the approach aloud
- [ ] Analyze time and space complexity
- [ ] Test edge cases
- [ ] Re-solve after 1 day
- [ ] Re-solve after 3–7 days
- [ ] Re-solve after 2–4 weeks
