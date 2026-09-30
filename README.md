# DSA Patterns & Problem-Solving in Python

A structured, systematic repository for mastering Data Structures and Algorithms (DSA) patterns, writing production-grade Python 3 solutions, analyzing computational complexity, and preparing for technical interviews at top product-based companies.

---

## Table of Contents
- [Project Purpose](#project-purpose)
- [Learning Goals](#learning-goals)
- [Priority System (P0–P3)](#priority-system-p0p3)
- [Repository Structure](#repository-structure)
- [Master Navigation & Pattern Directory](#master-navigation--pattern-directory)
- [How to Navigate Patterns](#how-to-navigate-patterns)
- [How to Add a New Problem](#how-to-add-a-new-problem)
- [How to Record Solutions and Mistakes](#how-to-record-solutions-and-mistakes)
- [How to Track Revisions (Spaced Repetition)](#how-to-track-revisions-spaced-repetition)
- [Python Version & Execution Instructions](#python-version--execution-instructions)
- [Master Progress Tracker](#master-progress-tracker)

---

## Project Purpose
Most interview candidates fail not because they haven't seen enough questions, but because they memorize code rather than internalizing **underlying algorithmic patterns**. 

This repository serves as a personal, active-learning system designed to:
- Learn the core intuition and reusable templates behind every major DSA pattern.
- Implement idiomatic, optimal Python 3 solutions independently.
- Document thought processes, edge cases, trade-offs, and verbal interview explanations.
- Systematically log bugs, incorrect assumptions, and off-by-one errors to prevent repeating them.
- Enforce spaced repetition to ensure long-term retention.

---

## Learning Goals
1. **Pattern Recognition:** Identify the appropriate pattern within 2–3 minutes of reading an interview question.
2. **First-Principles Derivation:** Transition from brute-force ($O(N^2)$ or exponential) to optimal ($O(N)$ or $O(N \log N)$) through clear invariants.
3. **Interview Communication:** Articulate approach, complexities, and trade-offs concisely and confidently before writing code.
4. **Bug-Free Implementation:** Write clean, readable, modular Python 3 code with proper handling of all boundary conditions.

---

## Priority System (P0–P3)

To optimize interview preparation, patterns are categorized into four strategic priority tiers:

| Tier | Focus Area | Description |
| :---: | :--- | :--- |
| **P0** | **Core Interview Fundamentals** | The highest-yield patterns. Tested in ~70% of tech interviews. Covers array/string manipulation, hashing, two pointers, sliding window, binary search, stacks, queues, and recursion foundations. |
| **P1** | **High-Priority Interview Patterns** | Essential medium-to-hard patterns tested heavily across all product companies: linked lists, binary trees, BSTs, heaps, prefix sums, intervals, greedy, backtracking, and monotonic stacks. |
| **P2** | **Advanced Interview Preparation** | Rigorous patterns expected for mid/senior engineering roles and tier-1 product companies: graph traversals (BFS/DFS), topological sort, union-find, tries, dynamic programming, and bit manipulation. |
| **P3** | **Advanced Practice & Mastery** | Hard-level problems, multi-pattern compositions, advanced DP (bitmask/digit/tree), advanced graph algorithms (Dijkstra/MST), complex caches, and company-specific interview archives. |

---

## Repository Structure

```text
DSA-Patterns-Python/
│
├── README.md                           # Main repository dashboard and documentation
├── ROADMAP.md                          # 5-phase preparation roadmap and milestones
├── PROGRESS.md                         # Master progress metrics & problem counts
├── REVISION_LOG.md                     # Spaced repetition tracking log
├── .gitignore                          # Clean Python gitignore
│
├── 00-Python-Fundamentals/             # Language mastery, complexity, built-ins, recursion
│   ├── README.md
│   ├── complexity-analysis.md
│   ├── python-builtins-for-dsa.md
│   └── recursion-basics.md
│
├── P0-Core/                            # Core fundamentals (P0)
│   ├── README.md
│   ├── 01-Arrays-and-Strings/
│   ├── 02-Hashing/
│   ├── 03-Two-Pointers/
│   ├── 04-Sliding-Window/
│   ├── 05-Binary-Search/
│   ├── 06-Sorting/
│   ├── 07-Stack-and-Queue/
│   ├── 08-Two-Dimensional-Arrays/
│   └── 09-Basic-Recursion/
│
├── P1-High-Priority/                   # High-yield patterns (P1)
│   ├── README.md
│   ├── 01-Linked-List/
│   ├── 02-Trees-and-Binary-Trees/
│   ├── 03-Binary-Search-Tree/
│   ├── 04-Heap-and-Priority-Queue/
│   ├── 05-Prefix-Sum/
│   ├── 06-Intervals/
│   ├── 07-Greedy/
│   ├── 08-Backtracking/
│   └── 09-Monotonic-Stack/
│
├── P2-Advanced/                        # Advanced patterns (P2)
│   ├── README.md
│   ├── 01-Graphs/
│   ├── 02-Graph-Traversal-BFS-DFS/
│   ├── 03-Topological-Sort/
│   ├── 04-Union-Find/
│   ├── 05-Tries/
│   ├── 06-Dynamic-Programming/
│   ├── 07-Bit-Manipulation/
│   └── 08-Advanced-Trees/
│
├── P3-Advanced-Practice/               # Hard & specialized problems (P3)
│   ├── README.md
│   ├── 01-Advanced-Dynamic-Programming/
│   ├── 02-Advanced-Graphs/
│   ├── 03-Complex-Data-Structures/
│   ├── 04-Hard-Problems/
│   └── 05-Company-Specific/
│
├── Company-Preparation/                # Company-specific breakdown & interview insights
│   ├── README.md
│   ├── Accenture/
│   ├── Deloitte/
│   ├── IBM/
│   └── Product-Based-Companies/
│
└── Templates/                          # Reusable templates
    ├── pattern-notes-template.md       # Template for creating new pattern notes
    ├── problem-solution-template.md    # Template for individual problem documentation
    └── revision-template.md            # Template for logging review sessions
```

---

## Master Navigation & Pattern Directory

### Priority 0: Core Interview Fundamentals
| # | Pattern | Key Concepts | Notes Link |
| :-: | :--- | :--- | :---: |
| 01 | **Arrays and Strings** | In-place modifications, subarray indexing, string manipulation | [README](P0-Core/01-Arrays-and-Strings/README.md) |
| 02 | **Hashing** | Hash maps, hash sets, frequency counting, index lookups | [README](P0-Core/02-Hashing/README.md) |
| 03 | **Two Pointers** | Opposite directions, fast/slow, read/write, 3Sum, pair counting | [README](P0-Core/03-Two-Pointers/README.md) |
| 04 | **Sliding Window** | Fixed window, dynamic shrink/expand window, substring optimization | [README](P0-Core/04-Sliding-Window/README.md) |
| 05 | **Binary Search** | Midpoint calculation, monotonic search space, lower/upper bounds | [README](P0-Core/05-Binary-Search/README.md) |
| 06 | **Sorting** | QuickSelect, Dutch National Flag, custom comparator sorting | [README](P0-Core/06-Sorting/README.md) |
| 07 | **Stack and Queue** | LIFO matching, monotonic property, FIFO queue simulation | [README](P0-Core/07-Stack-and-Queue/README.md) |
| 08 | **Two-Dimensional Arrays** | Grid traversals, coordinate offsets, in-place matrix operations | [README](P0-Core/08-Two-Dimensional-Arrays/README.md) |
| 09 | **Basic Recursion** | Base cases, recursive call stack, divide-and-conquer fundamentals | [README](P0-Core/09-Basic-Recursion/README.md) |

### Priority 1: High-Priority Interview Patterns
| # | Pattern | Key Concepts | Notes Link |
| :-: | :--- | :--- | :---: |
| 01 | **Linked List** | Pointer reversal, fast-slow runners, dummy heads | [README](P1-High-Priority/01-Linked-List/README.md) |
| 02 | **Trees and Binary Trees** | DFS (pre/in/post-order), BFS (level order), tree diameter, LCA | [README](P1-High-Priority/02-Trees-and-Binary-Trees/README.md) |
| 03 | **Binary Search Tree** | BST invariant ($L < root < R$), validation, range queries | [README](P1-High-Priority/03-Binary-Search-Tree/README.md) |
| 04 | **Heap & Priority Queue** | Min-heap, max-heap, Top-K elements, streaming median | [README](P1-High-Priority/04-Heap-and-Priority-Queue/README.md) |
| 05 | **Prefix Sum** | Cumulative sums, subarray sum equals K, 2D range sum queries | [README](P1-High-Priority/05-Prefix-Sum/README.md) |
| 06 | **Intervals** | Interval merging, non-overlapping intervals, meeting room scheduling | [README](P1-High-Priority/06-Intervals/README.md) |
| 07 | **Greedy** | Locally optimal decisions, activity selection, jump games | [README](P1-High-Priority/07-Greedy/README.md) |
| 08 | **Backtracking** | State exploration, pruning, choose-explore-unchoose paradigm | [README](P1-High-Priority/08-Backtracking/README.md) |
| 09 | **Monotonic Stack** | Next greater element, daily temperatures, histogram area | [README](P1-High-Priority/09-Monotonic-Stack/README.md) |

### Priority 2: Advanced Interview Preparation
| # | Pattern | Key Concepts | Notes Link |
| :-: | :--- | :--- | :---: |
| 01 | **Graphs** | Adjacency list representation, degree, cycle detection | [README](P2-Advanced/01-Graphs/README.md) |
| 02 | **Graph Traversal BFS/DFS** | Connected components, flood fill, shortest path in unweighted graphs | [README](P2-Advanced/02-Graph-Traversal-BFS-DFS/README.md) |
| 03 | **Topological Sort** | Kahn's algorithm (indegree queue), cycle detection in DAGs | [README](P2-Advanced/03-Topological-Sort/README.md) |
| 04 | **Union-Find (DSU)** | Disjoint set union, path compression, union by rank | [README](P2-Advanced/04-Union-Find/README.md) |
| 05 | **Tries** | Prefix trees, autocomplete, string search with wildcards | [README](P2-Advanced/05-Tries/README.md) |
| 06 | **Dynamic Programming** | Optimal substructure, overlapping subproblems, 1D/2D memoization | [README](P2-Advanced/06-Dynamic-Programming/README.md) |
| 07 | **Bit Manipulation** | Bitwise operators, XOR cancellations, power-of-two tests, bitmasks | [README](P2-Advanced/07-Bit-Manipulation/README.md) |
| 08 | **Advanced Trees** | Segment trees, Fenwick trees (Binary Indexed Trees) concepts | [README](P2-Advanced/08-Advanced-Trees/README.md) |

### Priority 3: Advanced Practice & Hard Challenges
| # | Pattern | Key Concepts | Notes Link |
| :-: | :--- | :--- | :---: |
| 01 | **Advanced DP** | Digit DP, Bitmask DP, Tree DP, Subsequence optimization | [README](P3-Advanced-Practice/01-Advanced-Dynamic-Programming/README.md) |
| 02 | **Advanced Graphs** | Dijkstra's shortest path, Bellman-Ford, Floyd-Warshall, Prim/Kruskal | [README](P3-Advanced-Practice/02-Advanced-Graphs/README.md) |
| 03 | **Complex Data Structures** | LRU Cache, LFU Cache, Monotonic Deque, Ordered Map simulation | [README](P3-Advanced-Practice/03-Complex-Data-Structures/README.md) |
| 04 | **Hard Problems** | Multi-pattern composition, rigorous edge-case puzzles | [README](P3-Advanced-Practice/04-Hard-Problems/README.md) |
| 05 | **Company-Specific** | Curated questions from real technical interview loops | [README](P3-Advanced-Practice/05-Company-Specific/README.md) |

---

## How to Navigate Patterns
1. Choose a target pattern from the table above or the [Roadmap](ROADMAP.md).
2. Read the pattern's `README.md` to review:
   - When to use the pattern
   - Core intuition & mental models
   - The general Python algorithm template
   - Common edge cases and classic traps
3. Navigate into the pattern's `problems/` directory to practice individual problems.

---

## How to Add a New Problem
When you encounter a new question you want to practice:
1. Locate the pattern directory (e.g., `P0-Core/04-Sliding-Window/problems/`).
2. Copy `Templates/problem-solution-template.md` into the `problems/` folder with a kebab-case filename:
   ```bash
   # Example:
   cp Templates/problem-solution-template.md P0-Core/04-Sliding-Window/problems/01-longest-substring-without-repeating-characters.md
   ```
3. (Optional) Create a paired `.py` file for quick local testing:
   ```bash
   touch P0-Core/04-Sliding-Window/problems/01-longest-substring-without-repeating-characters.py
   ```
4. Fill in the problem statement, examples, and pattern recognition clues.
5. Update the pattern's `README.md` table and `PROGRESS.md` with the new problem count.

---

## How to Record Solutions and Mistakes
- **Document First:** Write down the brute force approach, time/space complexity, and why it's suboptimal.
- **Trace Invariants:** In Section 5 & 6 of the problem markdown, write down the step-by-step logic and dry run a small example.
- **Record Mistakes Realistically:** Under Section 8 (**Mistakes I Made**), honestly capture:
  - Did you miss an empty string or single-item edge case?
  - Did you increment/decrement a pointer in the wrong branch?
  - Did you assume inputs were sorted when they weren't?
- **Interview Pitch:** Fill out Section 10 (**Interview Explanation**) with the 60–90 second pitch you would give your interviewer.

---

## How to Track Revisions (Spaced Repetition)
- When a problem is solved, mark its status in `PROGRESS.md` and set a reminder in [REVISION_LOG.md](REVISION_LOG.md).
- Follow the spaced intervals:
  - **Day 1:** Re-solve without looking at your prior solution.
  - **Day 3–7:** Focus on explaining the approach aloud and handling edge cases without hints.
  - **Day 14–30:** Speed test: solve on a blank screen in 15–20 minutes.

---

## Python Version & Execution Instructions
- **Language:** Python 3.10+
- **External Dependencies:** None required (standard library only: `collections`, `heapq`, `bisect`, `math`, `typing`).

### Running a Problem Solution Locally
```bash
# Navigate to the workspace root and run any problem file directly:
python P0-Core/03-Two-Pointers/problems/01-two-sum-ii.py

# Or run with Python 3:
python3 P0-Core/03-Two-Pointers/problems/01-two-sum-ii.py
```

---

## Master Progress Tracker
👉 View your overall preparation statistics, solved problem counts, and revision queue in [PROGRESS.md](PROGRESS.md).
