# Python Built-ins & Standard Library for DSA

Python provides an exceptionally rich standard library for competitive programming and interview problem-solving. Knowing the exact operation time complexities prevents accidental performance penalties.

---

## 1. Lists (`list`) — Dynamic Arrays

| Operation | Syntax | Time Complexity | Notes |
| :--- | :--- | :---: | :--- |
| Indexing | `nums[i]` | $O(1)$ | Direct memory address offset |
| Append | `nums.append(x)` | $O(1)$ amortized | Appends to end of array |
| Pop right | `nums.pop()` | $O(1)$ | Removes from end |
| Pop left | `nums.pop(0)` | **$O(N)$** | Shifts all elements left (avoid for queue!) |
| Insert | `nums.insert(i, x)` | $O(N)$ | Shifts elements from index `i` |
| Delete by value | `nums.remove(x)` | $O(N)$ | Linear search + shift |
| Slice | `nums[a:b]` | $O(b - a)$ | Copies elements to a new list |
| Sort | `nums.sort()` | $O(N \log N)$ | In-place Timsort |
| Reverse | `nums.reverse()` | $O(N)$ | In-place pointer swap |
| Length | `len(nums)` | $O(1)$ | Cached attribute |

> **Interview Tip:** Never use `nums.pop(0)` or `nums.insert(0, val)` in an iterative loop—it degrades an algorithm from $O(N)$ to $O(N^2)$. Use `collections.deque` instead.

---

## 2. Double-Ended Queue (`collections.deque`)

Implemented as a doubly-linked list of fixed-size memory blocks. Perfect for BFS and Queue operations.

```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)       # O(1) - append right
queue.appendleft(0)   # O(1) - append left
val = queue.popleft() # O(1) - pop left (Standard queue FIFO)
val = queue.pop()     # O(1) - pop right
```

| Operation | Time Complexity |
| :--- | :---: |
| `append(x)` / `appendleft(x)` | $O(1)$ |
| `pop()` / `popleft()` | $O(1)$ |
| Random Access `q[i]` | $O(N)$ (Avoid random access on deque) |

---

## 3. Dictionaries & Sets (`dict`, `set`)

Backed by internal open-addressing hash tables.

```python
# Hash Map
freq = {}
freq[key] = freq.get(key, 0) + 1  # Safe lookup with default

# collections.defaultdict
from collections import defaultdict
graph = defaultdict(list)
graph[u].append(v)  # Automatically initializes [] if u missing

# collections.Counter
from collections import Counter
counts = Counter("abracadabra") # counts['a'] -> 5
```

| Operation | Average Time | Worst Case Time | Notes |
| :--- | :---: | :---: | :--- |
| Lookup / Insert (`d[k]`, `s.add(x)`) | $O(1)$ | $O(N)$ | High collisions trigger $O(N)$ |
| Deletion (`del d[k]`, `s.remove(x)`) | $O(1)$ | $O(N)$ | |
| Membership check (`x in s`, `k in d`) | $O(1)$ | $O(N)$ | Much faster than `x in list` ($O(N)$) |

---

## 4. Priority Queue / Heap (`heapq`)

Python's `heapq` module provides a **Min-Heap** on top of a standard list.

```python
import heapq

nums = [5, 1, 8, 3]
heapq.heapify(nums)          # O(N) linear time construction!

heapq.heappush(nums, 2)      # O(log N) insertion
smallest = heapq.heappop(nums) # O(log N) removes smallest element

# Max-Heap idiom: Negate values
max_heap = [-x for x in nums]
heapq.heapify(max_heap)
largest = -heapq.heappop(max_heap)
```

---

## 5. Binary Search (`bisect`)

Built-in bisection algorithms for sorted lists.

```python
import bisect

arr = [1, 2, 4, 4, 4, 7, 9]

# bisect_left: First index where target can be inserted to maintain order
idx_left = bisect.bisect_left(arr, 4)   # Returns 2 (first 4)

# bisect_right: Index just after the last occurrence of target
idx_right = bisect.bisect_right(arr, 4) # Returns 5 (after last 4)
```

Time Complexity: $O(\log N)$ for search, but $O(N)$ if inserting via `bisect.insort()`.
