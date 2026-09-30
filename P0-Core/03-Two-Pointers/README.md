# Pattern: Two Pointers

## 1. Pattern Overview
The **Two Pointers** pattern uses two index references to traverse a data structure (typically a linear array, string, or linked list) simultaneously. Instead of exhaustively testing all pairs using nested loops ($O(N^2)$), the two pointers leverage sorted order, directional invariants, or speed differences to evaluate candidate solutions in linear $O(N)$ time.

---

## 2. What Problem Does This Pattern Solve?
- Eliminates nested loops when finding pairs, triplets, or subsegments satisfying specific sum or difference constraints.
- Replaces auxiliary memory structures by modifying arrays in-place ($O(1)$ space).
- Detects cycles or finds midpoints in single-pass iterations (Fast and Slow pointers).

---

## 3. When Should I Use This Pattern?
- The input array or string is **sorted** (or can be sorted in $O(N \log N)$ time without violating requirements).
- You need to search for pairs or triplets satisfying conditions (e.g., `nums[i] + nums[j] == target`).
- In-place modifications are required (e.g., removing duplicates, partitioning elements, shifting zeros).
- Searching for symmetric properties (e.g., palindrome validation).

---

## 4. How to Identify the Pattern from a Question
### Keyword Clues & Signals
- *"Sorted array"*, *"sorted list"*, *"find a pair with target sum"*.
- *"In-place"*, *"without allocating extra memory"*, *"Dutch national flag"*.
- *"Valid palindrome"*, *"reverse words / characters"*.
- *"Count pairs or triplets where sum is less than target"*.

### Problem Constraints
- $N \ge 10^5 \implies$ An $O(N^2)$ brute-force approach will get Time Limit Exceeded (TLE). A sorted $O(N)$ or $O(N \log N)$ two-pointer solution is required.

---

## 5. Core Intuition
In a sorted array, moving the left pointer to the right *strictly increases* the sum, while moving the right pointer to the left *strictly decreases* the sum. 

This directional monotonicity allows us to eliminate an entire row or column of search space with a single pointer increment/decrement, transforming an $O(N^2)$ grid search into an $O(N)$ line traversal.

---

## 6. Major Variations & Reusable Python Templates

### Variation 1: Opposite-Direction Pointers (Convergence)
Pointers start at opposite ends (`left = 0`, `right = len(arr) - 1`) and move toward each other.
- **Used for:** Two Sum in sorted arrays, Palindrome checking, Container with Most Water.

```python
def opposite_direction_template(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need a larger sum -> move left rightward
        else:
            right -= 1 # Need a smaller sum -> move right leftward
            
    return []
```

---

### Variation 2: Same-Direction / Fast-Slow Pointers
Both pointers start at the beginning and move in the same direction at different speeds.
- **Used for:** Linked list cycle detection, finding list middle, finding duplicates.

```python
def fast_slow_template(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Cycle detected
            
    return False
```

---

### Variation 3: Read-Write Pointers (In-Place Array Modification)
One pointer reads elements sequentially while the other writes valid elements to the front.
- **Used for:** Remove Duplicates from Sorted Array, Move Zeroes, In-place filtering.

```python
def read_write_template(nums):
    if not nums:
        return 0
        
    write = 1
    for read in range(1, len(nums)):
        # Check condition against previously accepted element
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
            
    return write  # New logical length
```

---

### Variation 4: Two Pointers After Sorting
When the original array is unsorted and index positions do not need to be preserved.
- **Used for:** 2Sum (values only), 2Sum Closest, Pair with target difference.

```python
def two_pointers_after_sort(nums, target):
    nums.sort()  # O(N log N)
    left, right = 0, len(nums) - 1
    
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return (nums[left], nums[right])
        elif s < target:
            left += 1
        else:
            right -= 1
    return None
```

---

### Variation 5: Three-Pointer Variations (e.g., 3Sum & Sort Colors)
- **3Sum:** Fix one index $i$, then run two-pointer convergence on the remaining subarray $[i+1, n-1]$.
- **Sort Colors (Dutch National Flag):** Three pointers (`low`, `mid`, `high`) partitioning elements into 3 buckets.

```python
def three_sum_template(nums):
    nums.sort()
    n = len(nums)
    triplets = []
    
    for i in range(n - 2):
        # Skip duplicate values for the fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                # Skip duplicate elements for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    return triplets
```

---

### Variation 6: Counting Pairs or Triplets Efficiently
Exploits sorted order to count multiple matching configurations in $O(1)$ instead of enumerating them individually.
- **Used for:** Count Triplets with Sum Smaller Than Target, Subarrays with bounded products.

```python
def count_triplets_smaller(nums, target):
    nums.sort()
    count = 0
    n = len(nums)
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] < target:
                # If sum is < target, all elements between left and right paired with i & left will also be < target
                count += (right - left)
                left += 1
            else:
                right -= 1
                
    return count
```

---

## 7. Step-by-Step Algorithm (General Opposite-Direction)
1. **Sort Input (if needed):** Sort array in non-decreasing order if preserving original indices is not required.
2. **Initialize Pointers:** Set `left = 0` and `right = len(arr) - 1`.
3. **Loop Condition:** While `left < right`:
   - Compute current metric (e.g., `arr[left] + arr[right]`).
   - If condition met: record answer or return indices. Update pointers while skipping consecutive duplicates.
   - If metric too small: increment `left` to increase value.
   - If metric too large: decrement `right` to decrease value.
4. **Return Result:** Return aggregated result or indicator if no match found.

---

## 8. Time and Space Complexity
- **Time Complexity:**
  - Already Sorted: $O(N)$ as each pointer moves at most $N$ steps.
  - Requires Sorting: $O(N \log N)$ dominated by Python's Timsort.
  - 3-Pointer (3Sum): $O(N^2)$ (Outer loop runs $N$ times, inner two pointers run $O(N)$).
- **Space Complexity:**
  - $O(1)$ auxiliary memory (in-place pointers).

---

## 9. Common Edge Cases
- Array length less than required elements ($N < 2$ for pairs, $N < 3$ for triplets).
- All elements identical (`[0, 0, 0, 0]` with target `0`).
- No valid pair/triplet exists.
- Inputs containing negative integers or zeroes.
- Array with extreme integer limits where overflow could occur in other languages.

---

## 10. Common Mistakes & Debugging Notes
- **Missing Duplicate Skipping:** Forgetting to skip duplicates when searching for unique triplets leading to duplicate answers.
- **Pointer Invalidation:** Incrementing `left` or decrementing `right` past bounds or past each other without checking `left < right`.
- **Modifying Array while Iterating:** Mutating array indices while relying on dynamic length.
- **Using `<` vs `<=`:** In two-sum, elements must be distinct indices, so `left < right`. In palindrome checks, either works.

---

## 11. Brute Force vs Optimized Approach

| Aspect | Brute Force (Nested Loops) | Optimized Two Pointers |
| :--- | :--- | :--- |
| **Two Sum Pair Search** | $O(N^2)$ time, $O(1)$ space | $O(N \log N)$ (or $O(N)$ if pre-sorted), $O(1)$ space |
| **Three Sum Search** | $O(N^3)$ time, $O(1)$ space | $O(N^2)$ time, $O(1)$ space |
| **In-place Filtering** | $O(N)$ extra space or $O(N^2)$ shift | $O(N)$ time, $O(1)$ space |

---

## 12. Comparison with Related Patterns

| Pattern | Relationship | When to choose Two Pointers over others |
| :--- | :--- | :--- |
| **Hash Map** | Both solve pair sum problems | Use Two Pointers when space must be $O(1)$ and array is sorted (or sortable). Use Hash Map when original indices must be preserved without sorting. |
| **Sliding Window** | Sub-category of two pointers | Use Sliding Window when maintaining a contiguous subsegment/subarray property. Use Two Pointers when indices converge or jump. |
| **Binary Search** | Can find pair complement | Two Pointers is $O(N)$ after sort, whereas Binary Search for each element is $O(N \log N)$. |

---

## 13. Problems to Solve

| # | Problem | Difficulty | Variation | Status | Markdown File | Python Solution |
| :-: | :--- | :---: | :--- | :---: | :--- | :--- |
| 1 | Two Sum II — Input Array Is Sorted | Medium | Opposite-direction | Not Started | [01-two-sum-ii.md](problems/01-two-sum-ii.md) | [01-two-sum-ii.py](problems/01-two-sum-ii.py) |
| 2 | Remove Duplicates from Sorted Array | Easy | Read-write pointer | Not Started | [02-remove-duplicates-from-sorted-array.md](problems/02-remove-duplicates-from-sorted-array.md) | [02-remove-duplicates-from-sorted-array.py](problems/02-remove-duplicates-from-sorted-array.py) |
| 3 | 3Sum | Medium | Fixed index + Converging | Not Started | [03-three-sum.md](problems/03-three-sum.md) | [03-three-sum.py](problems/03-three-sum.py) |
| 4 | 3Sum Closest | Medium | Fixed index + Converging | Not Started | [04-three-sum-closest.md](problems/04-three-sum-closest.md) | [04-three-sum-closest.py](problems/04-three-sum-closest.py) |
| 5 | Count Triplets with Sum Smaller Than a Target | Medium | Triplet counting | Not Started | [05-count-triplets-with-sum-less-than-target.md](problems/05-count-triplets-with-sum-less-than-target.md) | [05-count-triplets-with-sum-less-than-target.py](problems/05-count-triplets-with-sum-less-than-target.py) |
| 6 | Sort Colors | Medium | 3-way partition (Dutch National Flag) | Not Started | [06-sort-colors.md](problems/06-sort-colors.md) | [06-sort-colors.py](problems/06-sort-colors.py) |

---

## 14. Revision Checklist
- [ ] Understand when to sort vs when not to sort.
- [ ] Can handle duplicate skipping logic for 3Sum effortlessly.
- [ ] Master in-place read/write pointer mechanics without off-by-one errors.
- [ ] Know the difference between `(right - left)` pair counting and single element advancement.

---

## 15. Links to Individual Problem Files
- [01 - Two Sum II — Input Array Is Sorted](problems/01-two-sum-ii.md)
- [02 - Remove Duplicates from Sorted Array](problems/02-remove-duplicates-from-sorted-array.md)
- [03 - 3Sum](problems/03-three-sum.md)
- [04 - 3Sum Closest](problems/04-three-sum-closest.md)
- [05 - Count Triplets with Sum Smaller Than a Target](problems/05-count-triplets-with-sum-less-than-target.md)
- [06 - Sort Colors](problems/06-sort-colors.md)
