Absolutely! Below are **handwritten-style notes** that you can literally copy into your notebook. They are written exactly the way toppers make DSA interview notes—short, visual, and easy to revise.

---

# 📒 DSA NOTES - ARRAY & PYTHON LIST

---

# 1. What is an Array?

An **Array** is a collection of elements stored in **contiguous (continuous) memory locations**.

```
Index
 0    1    2    3    4
+----+----+----+----+----+
| 10 | 20 | 30 | 40 | 50 |
+----+----+----+----+----+
```

Each element has an index.

```
arr[0] = 10
arr[3] = 40
```

---

# 2. Why is Array Access O(1)?

Suppose

```
Base Address = 1000

Element Size = 4 bytes
```

```
Index      Address

0          1000

1          1004

2          1008

3          1012

4          1016
```

To access

```
arr[3]
```

CPU calculates

```
Address = Base Address + (Index × Element Size)

=1000+(3×4)

=1012
```

No searching.

Direct calculation.

✅ Time = **O(1)**

---

# 3. Why Insert is O(n)?

Suppose

```
10 20 30 40
```

Insert

```
5
```

at index 0

```
Before

10 20 30 40

↓

After

5 10 20 30 40
```

Need to shift

```
40 →

30 →

20 →

10 →
```

Everything moves.

Time = **O(n)**

---

# 4. Static Array vs Dynamic Array

### Static Array

```
Fixed Size

Cannot Grow
```

Example

```
int arr[5];
```

---

### Dynamic Array

Can increase automatically.

Python List is a **Dynamic Array**.

```
nums=[]

nums.append(10)
```

No fixed size.

---

# 5. Python List Memory

Suppose

```
nums=[10,20,30]
```

Python may allocate

```
Length = 3

Capacity = 6
```

```
Index

0   1   2    3      4      5

10 20 30 Empty Empty Empty
```

Length

```
Actual elements

3
```

Capacity

```
Allocated Space

6
```

---

# 6. append()

```
append(40)
```

```
Before

10 20 30 Empty Empty Empty

↓

After

10 20 30 40 Empty Empty
```

Nothing shifts.

Only inserted into empty slot.

✅ Average = **O(1)**

---

# 7. When append becomes O(n)?

Suppose

```
Capacity = 6

Length = 6
```

```
10 20 30 40 50 60
```

Now

```
append(70)
```

No space.

Python

### Step 1

Creates larger memory

```
Empty Empty Empty Empty Empty Empty Empty Empty Empty Empty Empty Empty
```

### Step 2

Copies

```
10

20

30

40

50

60
```

### Step 3

Insert

```
70
```

Copying all elements

Time = **O(n)**

But resizing happens rarely.

Therefore

```
append()

Average = O(1)

Worst = O(n)
```

This is called

```
Amortized O(1)
```

---

# 8. Big-O Symbols

Suppose

```
nums

10 20 30 40 50
```

```
n = 5
```

means

```
Total number of elements
```

---

Suppose

```
nums.extend([60,70,80])
```

```
k = 3
```

means

```
Number of inserted elements
```

---

Suppose

```
a=[1,2,3]

b=[4,5]
```

```
n =3

m =2
```

---

# Python List Methods

---

## append()

```
nums.append(10)
```

Time

```
Average O(1)

Worst O(n)
```

Reason

```
Insert at end.

No shifting.

Only resize occasionally.
```

---

## extend()

```
nums.extend([1,2,3])
```

```
k = inserted elements
```

Time

```
O(k)
```

Example

```
nums

10 20

↓

10 20 30 40 50
```

Need to copy only

```
30

40

50
```

---

## insert()

```
insert(index,value)
```

Example

```
10 20 30 40

↓

insert(1,15)

↓

10 15 20 30 40
```

Need to shift

```
20 →

30 →

40 →
```

Time

```
O(n)
```

---

## pop()

### pop()

```
10 20 30 40

↓

10 20 30
```

Time

```
O(1)
```

---

### pop(index)

```
10 20 30 40

↓

pop(1)

↓

10 30 40
```

Need shifting.

Time

```
O(n)
```

---

## remove()

```
remove(30)
```

Python

Search

↓

Shift

Time

```
O(n)
```

---

## clear()

Deletes every element.

Time

```
O(n)
```

---

## index()

```
index(50)
```

Search

```
10

20

30

40

50
```

Time

```
O(n)
```

---

## count()

```
count(2)
```

Need to check every element.

Time

```
O(n)
```

---

## reverse()

```
1 2 3 4 5

↓

5 4 3 2 1
```

Swap

```
1 ↔ 5

2 ↔ 4
```

Time

```
O(n)
```

---

## sort()

Python uses

```
Timsort
```

Time

```
O(n log n)
```

---

## copy()

```
a=[1,2,3]

b=a.copy()
```

Need to copy

```
1

2

3
```

Time

```
O(n)
```

---

## len()

```
len(nums)
```

Python already stores

```
Length
```

No counting.

Time

```
O(1)
```

---

## in Operator

```
30 in nums
```

Search

```
10

20

30
```

Time

```
O(n)
```

---

## Slice

```
nums[2:7]
```

Suppose

```
30 40 50 60 70
```

Need to copy

```
5 elements
```

```
k=5
```

Time

```
O(k)
```

---

## Concatenation

```
a+b
```

Need to copy

```
All elements of a

+

All elements of b
```

Time

```
O(n+m)
```

---

## max()

Checks every element.

```
O(n)
```

---

## min()

Checks every element.

```
O(n)
```

---

## sum()

Adds every element.

```
O(n)
```

---

# 🎯 Interview Cheat Sheet

| Method              | Time Complexity | Reason                           |
| ------------------- | --------------- | -------------------------------- |
| Access (`arr[i]`)   | O(1)            | Direct address calculation       |
| Update (`arr[i]=x`) | O(1)            | Direct overwrite                 |
| `append()`          | O(1) amortized  | Insert at end, occasional resize |
| `extend()`          | O(k)            | Copy only the new `k` elements   |
| `insert()`          | O(n)            | Shift elements right             |
| `pop()`             | O(1)            | Remove last element              |
| `pop(i)`            | O(n)            | Shift elements left              |
| `remove()`          | O(n)            | Search + shift                   |
| `clear()`           | O(n)            | Remove all elements              |
| `index()`           | O(n)            | Linear search                    |
| `count()`           | O(n)            | Scan all elements                |
| `reverse()`         | O(n)            | Swap elements                    |
| `sort()`            | O(n log n)      | Timsort                          |
| `copy()`            | O(n)            | Copy all elements                |
| `len()`             | O(1)            | Length stored internally         |
| `in`                | O(n)            | Linear search                    |
| `slice`             | O(k)            | Copy only `k` sliced elements    |
| `+`                 | O(n + m)        | Copy both lists                  |
| `max()`             | O(n)            | Visit all elements               |
| `min()`             | O(n)            | Visit all elements               |
| `sum()`             | O(n)            | Visit all elements               |

---

## ⭐ DSA Interview Tips (Must Remember)

1. **Python List = Dynamic Array** (not a linked list).
2. **Arrays store elements in contiguous memory.**
3. **Access by index is O(1)** because the address is calculated directly.
4. **`append()` is amortized O(1)** because Python over-allocates memory and resizes only occasionally.
5. **Any operation that requires shifting elements is O(n)** (`insert`, `pop(i)`, `remove`).
6. **Any operation that scans every element is O(n)** (`search`, `count`, `max`, `min`, `sum`).
7. **`sort()` uses Timsort with O(n log n)** average and worst-case time complexity.

Excellent question. The answer is:

> **You don't decide the capacity in Python. Python decides it automatically.**

This is one of the biggest differences between **Python lists** and **arrays in C/C++**.

---

# In C

You decide the capacity.

```c
int arr[10];
```

Capacity

```text
10
```

If you try

```c
arr[10] = 5;
```

❌ Error (out of bounds).

---

# In Python

```python
nums = []
```

You never write

```python
capacity = 10
```

Python internally decides how much memory to allocate.

---

# How does Python decide the capacity?

CPython (the standard Python implementation) **over-allocates** memory.

Instead of allocating exactly the required space, it allocates **a little extra** so that future `append()` operations are fast.

Example (illustrative):

```python
nums = []
```

Internally

```text
Length = 0
Capacity = 0
```

After

```python
nums.append(10)
```

Python may allocate more than one slot.

```text
Length = 1
Capacity = 4
```

After

```python
nums.append(20)
nums.append(30)
nums.append(40)
```

```text
Length = 4
Capacity = 4
```

Still okay.

Now

```python
nums.append(50)
```

Python notices

```text
Length == Capacity
```

So it allocates a larger block.

For example

```text
Length = 5
Capacity = 8
```

---

# Does capacity always double?

Many tutorials say:

```text
4 → 8 → 16 → 32
```

This is **not exactly true for Python**.

Python **doesn't simply double** the capacity like Java's `ArrayList` or C++'s `vector` often do.

Instead, CPython uses an **over-allocation strategy**.

The actual formula (simplified) is approximately:

```text
new_capacity = new_size + new_size/8 + a small constant
```

This means the capacity grows by roughly **12.5% plus a few extra slots**, not by exactly 2×.

---

# Real Example

Let's inspect how Python actually grows a list.

```python
import sys

nums = []

for i in range(20):
    nums.append(i)
    print(len(nums), sys.getsizeof(nums))
```

Sample output (values vary by Python version and platform):

```text
Length   Size (bytes)

0        56
1        88
2        88
3        88
4        88
5        120
6        120
7        120
8        120
9        184
...
```

Notice:

* The size doesn't increase after every append.
* It increases only when Python needs more capacity.

---

# Can we see the capacity directly?

No.

Python **does not expose the capacity** of a list.

You can only see:

```python
len(nums)
```

which returns

```text
Length
```

There is **no built-in function** like:

```python
capacity(nums)
```

---

# Then how do people know the capacity?

CPython stores it internally in its `PyListObject` structure.

Conceptually, it looks like this:

```text
PyListObject

Pointer ---> Memory Block

Length = 5

Allocated Capacity = 8
```

The `allocated` field is **internal to CPython** and is not part of Python's public API.

---

# Interview Answer

**Interviewer:** *"How do you decide the capacity of a Python list?"*

A good answer is:

> "You don't. Python lists are dynamic arrays. Python automatically manages the underlying capacity using an over-allocation strategy. As the list grows, it allocates additional memory in advance to reduce the number of expensive reallocations. This is why `append()` has an amortized time complexity of O(1)."

---

## Quick Comparison

| Language          | Who decides capacity?                              |
| ----------------- | -------------------------------------------------- |
| C Array           | Programmer                                         |
| C++ `vector`      | Library (automatic, but you can call `reserve()`)  |
| Java `ArrayList`  | Library (automatic, initial capacity configurable) |
| **Python `list`** | **Python runtime automatically**                   |

This automatic memory management is one of the reasons Python lists are so convenient, while still providing efficient append operations on average.

Excellent question. This is an **interview-level question**. Most people know `extend()` is **O(k)**, but very few know **what actually happens in memory**.

---

# First, what does `extend()` do?

```python
nums = [10, 20, 30]

nums.extend([40, 50, 60])
```

Result

```python
[10,20,30,40,50,60]
```

Unlike `append()`, which adds **one** element,

```python
nums.append(40)
```

`extend()` adds **multiple** elements one by one.

---

# Case 1: Enough Capacity Available

Suppose internally

```text
Length = 3
Capacity = 8
```

Memory

```text
Index

0      1      2      3      4      5      6      7

10     20     30   Empty  Empty  Empty  Empty  Empty
```

Now

```python
nums.extend([40,50,60])
```

Python checks

```text
How many new elements?

k = 3
```

Current free slots

```text
Capacity - Length

8 - 3

= 5 free slots
```

Need

```text
3 slots
```

Already available.

So Python simply copies

```text
40

50

60
```

into empty locations.

Final Memory

```text
Index

0      1      2      3      4      5      6      7

10     20     30     40     50     60   Empty  Empty
```

No old element moves.

Only three writes happen.

Time

```text
O(k)

k = inserted elements
```

---

# Case 2: Capacity is NOT Enough

Suppose

```text
Length = 6

Capacity = 8
```

Memory

```text
10 20 30 40 50 60 Empty Empty
```

Now

```python
nums.extend([70,80,90,100])
```

Need

```text
4 new slots
```

Available

```text
2 slots
```

Not enough.

---

## Step 1

Python allocates a larger memory block.

Suppose new capacity becomes 16.

New memory

```text
Empty Empty Empty Empty Empty Empty Empty Empty
Empty Empty Empty Empty Empty Empty Empty Empty
```

---

## Step 2

Copy all existing elements

Old

```text
10

20

30

40

50

60
```

↓

New

```text
10

20

30

40

50

60
```

---

## Step 3

Copy new elements

```text
70

80

90

100
```

Final

```text
10 20 30 40 50 60 70 80 90 100
```

---

# Why is extend() O(k) then?

This is the interesting part.

Suppose

```python
nums.extend([1,2,3,4,5])
```

Python performs something conceptually like:

```python
for item in [1,2,3,4,5]:
    nums.append(item)
```

But internally, it is **more optimized** than literally calling `append()` five times.

Instead, Python:

1. Determines the iterable's length (if possible).
2. Checks if there is enough capacity.
3. If not, **resizes once**.
4. Copies all new elements into consecutive memory locations.

So instead of:

```text
append()
↓

resize

↓

append()

↓

resize

↓

append()

↓

resize
```

it does

```text
Resize once

↓

Copy everything together
```

That's why `extend()` is efficient.

---

# Why isn't extend() O(n + k)?

Let's understand with an example.

Suppose

```python
nums = [10,20,30]
```

Current

```text
Length = 3

Capacity = 10
```

Now

```python
nums.extend([40,50,60])
```

Python does **not** touch

```text
10

20

30
```

It only copies

```text
40

50

60
```

Three copies.

Therefore

```text
Time = O(k)
```

where

```text
k = number of inserted elements
```

---

# But what if resizing happens?

Suppose

```python
nums.extend([1,2,3,4,5,6,7])
```

Now Python must

* allocate new memory
* copy **old elements**
* copy **new elements**

Technically, that single operation costs

```text
O(n + k)
```

because:

* `n` = existing elements copied
* `k` = new elements copied

However, just like `append()`, Python **over-allocates** memory. Resizing doesn't happen on every `extend()`, so across many operations the **amortized** complexity is still considered **O(k)**.

---

# Interview Answer ⭐

If an interviewer asks:

> **"How does `extend()` work internally?"**

A strong answer is:

> "`extend()` adds multiple elements from an iterable. Python first determines how many new elements will be added (when possible), checks whether the current list has enough unused capacity, and if needed allocates a larger memory block only once. It then copies the existing elements (only if a resize occurs) and finally copies all new elements into consecutive memory locations. When no resize is needed, only the new `k` elements are copied, so the complexity is O(k). If resizing occurs, that particular operation costs O(n + k), but due to Python's overallocation strategy, the amortized complexity is still O(k)."

This explanation demonstrates an understanding of **dynamic arrays**, **memory allocation**, **copying**, and **amortized analysis**, which is exactly what interviewers expect.


# 1. Time & Space Complexity

### Theory

* Big O
* Big Ω
* Big Θ
* Best Case
* Average Case
* Worst Case
* Amortized Analysis

### Questions

1. Calculate time complexity of nested loops
2. Calculate complexity of recursion
3. Analyze merge sort
4. Analyze quick sort
5. Complexity of hash table operations

---

# 2. Arrays

### Basics

1. Largest Element
2. Second Largest Element
3. Remove Duplicates
4. Move Zeroes
5. Rotate Array
6. Reverse Array
7. Check Sorted Array

### Intermediate

8. Two Sum
9. Best Time to Buy and Sell Stock
10. Majority Element
11. Kadane Algorithm
12. Rearrange Positive & Negative
13. Leaders in Array
14. Missing Number
15. Product of Array Except Self

### Advanced

16. Merge Intervals
17. Trapping Rain Water
18. Container With Most Water
19. Sliding Window Maximum
20. Maximum Product Subarray

---

# 3. Strings

### Basics

1. Reverse String
2. Palindrome
3. Anagram
4. Count Vowels
5. Remove Duplicates

### Intermediate

6. Longest Common Prefix
7. String Compression
8. Group Anagrams
9. Valid Parentheses
10. Longest Substring Without Repeating Characters

### Advanced

11. Minimum Window Substring
12. Rabin-Karp
13. KMP Algorithm
14. Z Algorithm
15. Manacher Algorithm

---

# 4. Searching

### Linear Search

1. Find Element
2. Count Occurrences

### Binary Search

3. Binary Search
4. Lower Bound
5. Upper Bound
6. First Occurrence
7. Last Occurrence
8. Search Insert Position

### Advanced

9. Search in Rotated Sorted Array
10. Find Peak Element
11. Median of Two Sorted Arrays
12. Kth Missing Positive Number

---

# 5. Sorting

### Basic Sorting

1. Bubble Sort
2. Selection Sort
3. Insertion Sort

### Efficient Sorting

4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Counting Sort
8. Radix Sort
9. Bucket Sort

### Questions

10. Sort Colors
11. Merge Sorted Arrays
12. Kth Largest Element

---

# 6. Recursion & Backtracking

### Recursion

1. Factorial
2. Fibonacci
3. Power Function
4. Tower of Hanoi

### Backtracking

5. Subsets
6. Permutations
7. Combination Sum
8. N-Queens
9. Rat in Maze
10. Sudoku Solver
11. Word Search

---

# 7. Linked List

### Singly Linked List

1. Reverse Linked List
2. Find Middle Node
3. Detect Loop
4. Remove Loop
5. Delete Node

### Advanced

6. Merge Two Sorted Lists
7. Intersection Point
8. Add Two Numbers
9. Copy Random Pointer
10. Reverse in K Groups
11. LRU Cache

### Doubly Linked List

12. Insert Node
13. Delete Node
14. Reverse DLL

---

# 8. Stack

### Basics

1. Implement Stack
2. Balanced Parentheses
3. Min Stack

### Advanced

4. Next Greater Element
5. Largest Rectangle in Histogram
6. Stock Span Problem
7. Infix to Postfix
8. Postfix Evaluation

---

# 9. Queue

### Basics

1. Implement Queue
2. Circular Queue

### Advanced

3. Sliding Window Maximum
4. First Non-Repeating Character
5. Implement Stack Using Queues
6. Implement Queue Using Stacks

---

# 10. Hashing

### Questions

1. Two Sum
2. Frequency Count
3. Longest Consecutive Sequence
4. Top K Frequent Elements
5. Subarray Sum Equals K
6. Happy Number

---

# 11. Trees

### Binary Tree

1. Inorder Traversal
2. Preorder Traversal
3. Postorder Traversal
4. Level Order Traversal
5. Height of Tree
6. Diameter of Tree
7. Balanced Tree

### Advanced

8. Lowest Common Ancestor
9. Zigzag Traversal
10. Vertical Traversal
11. Boundary Traversal
12. Serialize Deserialize Tree

---

# 12. Binary Search Tree (BST)

1. Search BST
2. Insert BST
3. Delete BST
4. Validate BST
5. Kth Smallest Element
6. LCA in BST
7. Recover BST

---

# 13. Heap / Priority Queue

1. K Largest Elements
2. Kth Largest Element
3. Merge K Sorted Lists
4. Top K Frequent Elements
5. Median Finder
6. Heap Sort

---

# 14. Graphs

### Traversal

1. BFS
2. DFS

### Cycle Detection

3. Undirected Graph Cycle
4. Directed Graph Cycle

### Topological Sort

5. Kahn's Algorithm
6. DFS Topological Sort

### Shortest Path

7. Dijkstra
8. Bellman Ford
9. Floyd Warshall

### MST

10. Prim's Algorithm
11. Kruskal Algorithm

### Advanced

12. Number of Islands
13. Clone Graph
14. Course Schedule
15. Word Ladder
16. Network Delay Time
17. Alien Dictionary

---

# 15. Greedy Algorithms

1. Activity Selection
2. Fractional Knapsack
3. Job Scheduling
4. Huffman Coding
5. Gas Station
6. Jump Game
7. Minimum Platforms

---

# 16. Dynamic Programming (Most Important)

### 1D DP

1. Fibonacci
2. Climbing Stairs
3. House Robber
4. Coin Change

### 2D DP

5. Unique Paths
6. Minimum Path Sum
7. Triangle Problem

### Strings DP

8. Longest Common Subsequence
9. Longest Palindromic Subsequence
10. Edit Distance

### Knapsack DP

11. 0/1 Knapsack
12. Unbounded Knapsack

### Advanced

13. Matrix Chain Multiplication
14. Partition Equal Subset Sum
15. Burst Balloons
16. Palindrome Partitioning

---

# 17. Tries

1. Implement Trie
2. Search Word
3. Word Dictionary
4. Maximum XOR Pair
5. Word Search II

---

# 18. Bit Manipulation

1. Check Odd Even
2. Power of Two
3. Count Set Bits
4. Single Number
5. Missing Number
6. Subsets Using Bits
7. XOR Problems

---

# 19. Segment Tree

1. Build Segment Tree
2. Range Sum Query
3. Range Minimum Query
4. Lazy Propagation

---

# 20. Disjoint Set Union (Union Find)

1. Find Operation
2. Union Operation
3. Number of Provinces
4. Kruskal Algorithm
5. Accounts Merge

---

# 21. Advanced Topics (Google/Meta Level)

1. Monotonic Stack
2. Monotonic Queue
3. Sparse Table
4. Fenwick Tree (BIT)
5. Suffix Array
6. Suffix Tree
7. Rolling Hash
8. Tarjan Algorithm
9. Kosaraju Algorithm
10. Heavy Light Decomposition
11. Meet in the Middle
12. Mo's Algorithm

---

# Most Asked LeetCode Problems (Must Do)

* Two Sum
* Valid Parentheses
* Merge Two Sorted Lists
* Best Time To Buy And Sell Stock
* Maximum Subarray
* Product Of Array Except Self
* Group Anagrams
* Longest Substring Without Repeating Characters
* Binary Tree Level Order Traversal
* Lowest Common Ancestor
* Number Of Islands
* Clone Graph
* Course Schedule
* Coin Change
* House Robber
* Longest Common Subsequence
* Kth Largest Element
* Merge Intervals
* Word Ladder
* LRU Cache


