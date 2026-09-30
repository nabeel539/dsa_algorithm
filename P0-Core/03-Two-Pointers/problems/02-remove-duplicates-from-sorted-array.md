# Remove Duplicates from Sorted Array

## Problem Details

* **Platform:** LeetCode (Problem #26)
* **Problem Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/
* **Difficulty:** Easy
* **Priority:** P0
* **Pattern:** Two Pointers (Read-Write / Fast-Slow)
* **Related Patterns:** In-place Array Operations
* **Status:** Not Started
* **Last Revised:** 

---

## 1. Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following:
1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present initially.
2. The remaining elements of `nums` do not matter.
3. Return `k`.

---

## 2. Examples

### Example 1
```text
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
```

### Example 2
```text
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4.
```

---

## 3. Pattern Recognition

* **What clues indicate this pattern?**
  - "In-place removal with $O(1)$ extra memory."
  - "Array is sorted in non-decreasing order."
  - "Return count of unique elements while preserving relative order."
* **Why is this pattern suitable?**
  - Since duplicates are adjacent in a sorted array, we can use a **write pointer** to keep track of the boundary of unique elements and a **read pointer** (fast pointer) to scan forward looking for new distinct values.

---

## 4. Brute Force Approach

* **Intuition:**
  - Convert list to a set to extract unique elements, sort the set, and copy back into `nums`. Or use a separate list.
* **Algorithm:**
  1. Store unique elements in an auxiliary list.
  2. Copy values back into the beginning of `nums`.
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$
* **Limitations:**
  - Violates the strict $O(1)$ auxiliary space constraint.

---

## 5. Optimized Approach

* **Intuition:**
  - Use two pointers: `write` pointer pointing to the index where the next unique element should be placed, and `read` iterating through the array.
* **Step-by-step Algorithm:**
  1. If `len(nums) == 0`, return 0.
  2. Set `write = 1` (the first element `nums[0]` is always uniquely positioned).
  3. Loop with `read` from index 1 to `len(nums) - 1`:
     - If `nums[read] != nums[write - 1]`:
       - Assign `nums[write] = nums[read]`
       - Increment `write += 1`
  4. Return `write`.
* **Python Code:**
  - See full implementation in [02-remove-duplicates-from-sorted-array.py](02-remove-duplicates-from-sorted-array.py).
* **Time Complexity:** $O(N)$ — Single scan through array.
* **Space Complexity:** $O(1)$ — In-place modification.

---

## 6. Dry Run

*Input:* `nums = [0, 0, 1, 1, 2]`

| Step | `read` | `nums[read]` | `write` | `nums[write - 1]` | Condition (`nums[read] != nums[write-1]`) | Action | Array State |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Init | - | - | 1 | 0 | - | - | `[0, 0, 1, 1, 2]` |
| 1 | 1 | 0 | 1 | 0 | False | Skip | `[0, 0, 1, 1, 2]` |
| 2 | 2 | 1 | 1 | 0 | True | `nums[1] = 1`, `write = 2` | `[0, 1, 1, 1, 2]` |
| 3 | 3 | 1 | 2 | 1 | False | Skip | `[0, 1, 1, 1, 2]` |
| 4 | 4 | 2 | 2 | 1 | True | `nums[2] = 2`, `write = 3` | `[0, 1, 2, 1, 2]` |

Final `write` = 3, unique elements = `[0, 1, 2]`.

---

## 7. Edge Cases

| Edge Case Scenario | Test Input | Expected Output | Outcome / Verified |
| :--- | :--- | :--- | :---: |
| Single element array | `nums = [1]` | `1, nums = [1]` | [ ] |
| All elements identical | `nums = [2, 2, 2, 2]` | `1, nums = [2, ...]` | [ ] |
| Already all unique | `nums = [1, 2, 3, 4]` | `4, nums = [1, 2, 3, 4]` | [ ] |
| Array with negative numbers | `nums = [-3, -3, -1, 0, 0]` | `3, nums = [-3, -1, 0, ...]` | [ ] |

---

## 8. Mistakes I Made

*(To be filled during active practice)*

---

## 9. What I Learned

*(To be filled in your own words after solving)*

---

## 10. Interview Explanation

> "Because the array is sorted, duplicate elements are always adjacent. We can solve this in-place in $O(N)$ time and $O(1)$ space using a two-pointer read-write technique. We maintain a `write` pointer at index 1 and scan with a `read` pointer from index 1. Whenever `nums[read]` differs from `nums[write - 1]`, we overwrite `nums[write]` with `nums[read]` and advance `write`. Finally, `write` represents the count of unique elements."

---

## 11. Revision

- [ ] Solve without looking at notes
- [ ] Explain the approach aloud
- [ ] Analyze time and space complexity
- [ ] Test edge cases
- [ ] Re-solve after 1 day
- [ ] Re-solve after 3–7 days
- [ ] Re-solve after 2–4 weeks
