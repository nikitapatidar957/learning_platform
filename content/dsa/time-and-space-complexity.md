This is the **foundation of DSA**. If you understand Time & Space Complexity well, solving DSA becomes much easier.

# 1. What is Time Complexity?

Time Complexity tells us **how the execution time grows as input size (n) increases**.

Example:

```python
for i in range(n):
    print(i)
```

If `n = 5`, loop runs 5 times.

If `n = 1000`, loop runs 1000 times.

Time Complexity:

```text
O(n)
```

---

# 2. What is Space Complexity?

Space Complexity tells us **how much extra memory is used**.

Example:

```python
arr = [0] * n
```

If n increases, memory usage also increases.

## 🧠 What is Space Complexity?

**Space complexity tells us how much extra memory an algorithm needs as the input size `n` increases.**

The important words are:

* **Space** → memory/RAM used
* **Complexity** → how that memory usage changes as `n` grows
* **`n`** → size of the input

### Simple example

Suppose:

```python
nums = [10, 20, 30, 40, 50]
```

Here `n = 5`.

If we change it to:

```python
nums = [10, 20, 30, ..., 1000000]
```

then `n = 1,000,000`.

The question for **space complexity** is:

> As `n` becomes bigger, does my algorithm need more memory?

---

# 1. O(1) — Constant Space

Memory does **not depend on `n`**.

```python
def get_first(nums):
    first = nums[0]
    return first
```

Suppose:

```text
n = 5
```

We create only one extra variable:

```text
first
```

For:

```text
n = 100
n = 10,000
n = 1,000,000
```

we still need approximately the same extra memory.

Therefore:

```text
Space Complexity = O(1)
```

### Another example

```python
def sum_two_numbers(a, b):
    result = a + b
    return result
```

Only a few variables → **O(1)**.

---

# 2. O(n) — Linear Space

Memory increases **proportionally with `n`**.

```python
def copy_array(nums):
    result = []

    for x in nums:
        result.append(x)

    return result
```

Suppose the input is:

```text
nums = [1, 2, 3, 4, 5]
```

The algorithm creates:

```text
result = [1, 2, 3, 4, 5]
```

If:

```text
n = 5      → result stores 5 elements
n = 100    → result stores 100 elements
n = 1000   → result stores 1000 elements
```

So memory grows with `n`.

```text
Space Complexity = O(n)
```

### Think of it like this:

```text
Input size       Extra memory

n = 5            5
n = 10            10
n = 100           100
n = 1000          1000
```

That's why we call it **linear space**.

---

# 3. O(n²) — Quadratic Space

Memory grows like:

```text
n × n
```

Example:

```python
def create_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    return matrix
```

If:

```text
n = 3
```

we create:

```text
[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

That's:

```text
3 × 3 = 9
```

For:

```text
n = 10 → 10 × 10 = 100
n = 100 → 100 × 100 = 10,000
n = 1000 → 1000 × 1000 = 1,000,000
```

Therefore:

```text
Space Complexity = O(n²)
```

---

# 4. O(log n) — Logarithmic Space

This commonly happens with **recursion where the problem size is divided**.

For example:

```python
def binary_search(nums, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        return binary_search(nums, target, left, mid - 1)

    return binary_search(nums, target, mid + 1, right)
```

Each recursive call reduces the search area by approximately half:

```text
n
↓
n/2
↓
n/4
↓
n/8
↓
n/16
...
```

How many times can we divide `n` by 2 until we reach 1?

That's approximately:

```text
log₂(n)
```

So the **recursion stack** uses:

```text
O(log n)
```

space.

> Important: **Iterative binary search** can use O(1) space, while **recursive binary search** uses O(log n) stack space.

---

# 5. O(n) Space Due to Recursion

You can also get linear space from recursion.

```python
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
```

For:

```text
n = 5
```

the calls are:

```text
print_numbers(5)
    ↓
print_numbers(4)
    ↓
print_numbers(3)
    ↓
print_numbers(2)
    ↓
print_numbers(1)
    ↓
print_numbers(0)
```

All these function calls remain in memory until the recursion starts returning.

So there are approximately `n` calls in the stack.

```text
Space Complexity = O(n)
```

This is called **recursion stack space**.

---

# 6. O(2ⁿ) — Exponential Space

A classic example is recursive Fibonacci:

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
```

The **time complexity** is exponential:

```text
O(2ⁿ)
```

But here's an important point:

### Its space complexity is NOT O(2ⁿ).

The recursion depth is only `n`, so the call stack uses:

```text
O(n)
```

This is a very important interview concept:

> **Time complexity and space complexity can be completely different.**

For this Fibonacci implementation:

```text
Time  = O(2ⁿ)
Space = O(n)
```

---

# 7. O(n²) Space with Strings

Consider:

```python
def make_strings(nums):
    result = []

    for i in range(len(nums)):
        s = ""

        for j in range(len(nums)):
            s += str(nums[j])

        result.append(s)

    return result
```

There are `n` strings, and each string can contain `n` characters.

So approximately:

```text
n strings × n characters
```

Therefore:

```text
O(n²)
```

space.

---

# ⭐ Most Important Comparison

| Space        | What it means                            | Example                                |
| ------------ | ---------------------------------------- | -------------------------------------- |
| **O(1)**     | Same amount of extra memory              | Few variables                          |
| **O(log n)** | Memory grows logarithmically             | Recursive binary search                |
| **O(n)**     | Memory grows with input                  | Copying an array / recursion           |
| **O(n²)**    | Memory grows as `n × n`                  | 2D matrix                              |
| **O(2ⁿ)**    | Memory doubles with each increase in `n` | Some recursive algorithms              |
| **O(n!)**    | Extremely rapid memory growth            | Algorithms generating all permutations |

---

# 🧠 How to Find Space Complexity

When you see code, ask:

### Step 1: What extra data structures are created?

```python
result = []
```

Potentially depends on `n` → **O(n)**.

---

### Step 2: How big can they become?

```python
result = []

for x in nums:
    result.append(x)
```

`result` can contain `n` elements.

Therefore:

```text
O(n)
```

---

### Step 3: Are there nested data structures?

```python
matrix = []

for i in range(n):
    row = []

    for j in range(n):
        row.append(0)

    matrix.append(row)
```

There are:

```text
n rows × n elements
```

Therefore:

```text
O(n²)
```

---

### Step 4: Is recursion being used?

Look at how deep the recursion can go.

```python
def fun(n):
    if n == 0:
        return

    fun(n - 1)
```

Depth:

```text
n → n-1 → n-2 → ... → 0
```

Therefore:

```text
O(n)
```

---

# 🚨 One Very Important Concept: Input Space vs Auxiliary Space

Suppose:

```python
def find_max(nums):
    maximum = nums[0]

    for x in nums:
        if x > maximum:
            maximum = x

    return maximum
```

The input itself takes memory:

```text
nums → O(n)
```

But we **didn't create another array**.

We only created:

```text
maximum → O(1)
x       → O(1)
```

Therefore:

### Auxiliary/extra space:

```text
O(1)
```

Usually, when DSA questions ask **"space complexity of the algorithm"**, they often mean **extra/auxiliary space**, excluding the memory already occupied by the input.

---

## 🎯 Easy way to remember

Think:

```text
O(1)      → "I need a few boxes."
O(log n)  → "I need a slowly increasing number of boxes."
O(n)      → "I need one box for every input."
O(n²)     → "I need a table of n × n boxes."
```

And the biggest trick:

> **For space complexity, don't look at how many times the code runs. Look at how much data stays stored in memory.**

For example:

```python
for i in range(n):
    print(i)
```

The loop runs `n` times, so **time = O(n)**.

But it doesn't store `n` things.

So:

```text
Time  = O(n)
Space = O(1)
```

That distinction is one of the most important things to understand before analyzing DSA code.


tell me what is space complexity here 
class Stack():
    def __init__(self):
        self.s = []
    def isEmpty(self):
        if self.s:
            return False
        return True
    def top(self):
        if self.isEmpty():
            return -1
        return self.s[-1]
        
    def pop(self):
        if self.isEmpty():
            return -1

        element = self.s[-1]
        del self.s[-1]
        return element
    def push(self,element):
        self.s.append(element)
    def traverse(self):
        if self.isEmpty():
            return -1
        for i in self.s:
            print(i)
    
    
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        arr = [0]*len(temperatures)
        s1 = Stack()
        for i in range(len(temperatures)):
            if not s1.isEmpty():
                
                while temperatures[s1.top()] < temperatures[i] and s1.isEmpty() == False:
                    element = s1.pop()
                    arr[element] = i-element
                    
            s1.push(i)
        return arr
        

Space Complexity:

```text
O(n)
```
Yes. Let's calculate the **space complexity of your exact code** step by step.

Let:

```text
n = len(temperatures)
```

Your important data structures are:

```python
arr = [0] * len(temperatures)
s1 = Stack()
```

## 1. `arr`

```python
arr = [0] * len(temperatures)
```

If `temperatures` has `n` elements:

```text
temperatures → n elements
arr          → n elements
```

So `arr` uses:

```text
O(n)
```

space.

---

## 2. `s1`

Your stack stores **indices**:

```python
s1.push(i)
```

In the worst case, the stack can contain almost/all `n` indices.

For example, if temperatures are decreasing:

```text
[90, 80, 70, 60, 50]
```

Nothing gets popped, so the stack becomes:

```text
[0, 1, 2, 3, 4]
```

That's `n` elements.

Therefore:

```text
s1 → O(n)
```

space.

---

## 3. Other variables

You also have:

```python
element
i
```

These are just individual variables.

They use:

```text
O(1)
```

space.

The `Stack` object itself is also constant overhead; its internal list is what grows to `O(n)`.

---

# Now combine them

You have:

```text
arr  → O(n)
s1   → O(n)
variables → O(1)
```

So:

```text
O(n) + O(n) + O(1)
```

Drop constants:

```text
O(n)
```

### ✅ Final answer

```text
Space Complexity = O(n)
```

---

## But there is one important distinction

Your function receives:

```python
temperatures
```

which is already an input array of size `n`.

We normally **don't count the input array** when calculating **auxiliary space**.

Your newly created memory is:

```text
arr → O(n)
s1  → O(n)
```

Therefore:

> **Auxiliary Space = O(n)**

If someone asks for **total space including the input**, you could say:

```text
Input temperatures → O(n)
Output arr         → O(n)
Stack              → O(n)

Total → O(n)
```

It is still **O(n)** because:

```text
O(n) + O(n) + O(n) = O(n)
```

---

# 🧠 Why isn't it O(n²)?

This is a very common confusion.

You have:

```python
for i in range(n):
    ...
    while ...:
        ...
```

You might think:

> "There is a `for` and a `while`, so space must be O(n²)."

❌ No.

**Nested loops primarily affect time, not automatically space.**

For space, ask:

> **How many elements can be stored at the same time?**

Your stack can hold at most `n` indices:

```text
s1 = [0, 1, 2, 3, ..., n-1]
```

And `arr` holds `n` values:

```text
arr = [0, 0, 0, ..., 0]
```

So maximum extra memory is proportional to `n`.

```text
              Space
                ↓
arr ────────── O(n)
stack ──────── O(n)
variables ──── O(1)
                ↓
             O(n)
```

### Final:

**Time Complexity:** `O(n)` amortized
**Auxiliary Space:** `O(n)`

The reason the time is `O(n)` despite the `while` inside the `for` is a separate but very important concept: **each index is pushed once and popped at most once**.



---

# 3. Big O Notation (Worst Case)

Big O represents the **maximum time an algorithm can take**.

### Example

```python
for i in range(n):
    print(i)
```

Runs n times.

```text
O(n)
```

### Example

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Runs:

```text
n × n = n²
```

Time Complexity:

```text
O(n²)
```

---

# Common Big O Values

| Complexity | Name         |
| ---------- | ------------ |
| O(1)       | Constant     |
| O(log n)   | Logarithmic  |
| O(n)       | Linear       |
| O(n log n) | Linearithmic |
| O(n²)      | Quadratic    |
| O(n³)      | Cubic        |
| O(2ⁿ)      | Exponential  |
| O(n!)      | Factorial    |

---

# 4. Big Ω (Omega) - Best Case

Represents the **minimum time** an algorithm can take.

Example:

```python
arr = [10,20,30,40]

target = 10
```

Linear Search:

```python
for i in arr:
    if i == target:
        return True
```

Target found at first position.

```text
Ω(1)
```

---

# 5. Big Θ (Theta) - Average/Tight Bound

Represents both upper and lower bound.

Example:

```python
for i in range(n):
    print(i)
```

Always runs n times.

```text
Θ(n)
```

---

# 6. Best, Average, Worst Case

Consider Linear Search:

```python
arr = [10,20,30,40,50]
```

Searching 10:

```text
Best Case = O(1)
```

Searching 30:

```text
Average Case = O(n/2)
≈ O(n)
```

Searching 50:

```text
Worst Case = O(n)
```
🧠 Super-easy memory trick

Remember the letters:

O → Outermost / Upper
O = upper bound
Ω → Minimum
Ω = lower bound
Θ → Tight
Θ = tight/exact growth
---
BIG-O
O(f(n))
→ Upper bound
→ "At most this growth"

BIG-OMEGA
Ω(f(n))
→ Lower bound
→ "At least this growth"

BIG-THETA
Θ(f(n))
→ Tight bound
→ "Grows at this rate"
| Complexity     | What to look for                 |
| -------------- | -------------------------------- |
| **O(1)**       | Fixed amount of work             |
| **O(log n)**   | Divide by a constant             |
| **O(n)**       | One pass through input           |
| **O(n log n)** | `n` work at `log n` levels       |
| **O(n²)**      | Two nested loops                 |
| **O(n³)**      | Three nested loops               |
| **O(2ⁿ)**      | 2 choices/branches per element   |
| **O(kⁿ)**      | `k` choices/branches per element |
| **O(n!)**      | All permutations/orderings       |


# 7. Amortized Analysis

Sometimes an operation is expensive occasionally, but cheap overall.

Example: Python List Append

```python
arr = []

arr.append(1)
arr.append(2)
arr.append(3)
```

Most appends:

```text
O(1)
```

Occasionally Python increases array size:

```text
O(n)
```

But average cost:

```text
Amortized O(1)
```

This is why list append is considered:

```text
O(1)
```

---

# Question 1: Nested Loops Complexity

### Example

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Outer loop:

```text
n times
```

Inner loop:

```text
n times
```

Total:

```text
n × n
```

Answer:

```text
O(n²)
```

---

### Example 2

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

Runs:

```text
1 + 2 + 3 + ... + n
```

Formula:

```text
n(n+1)/2
```

Ignore constants:

```text
O(n²)
```

---

### Example 3

```python
for i in range(n):
    for j in range(100):
        print(i, j)
```

100 is constant.

```text
n × 100
```

Answer:

```text
O(n)
```

---

# Question 2: Recursion Complexity

### Example

```python
def fun(n):
    if n == 0:
        return

    fun(n-1)
```

Calls:

```text
n → n-1 → n-2 → ... → 0
```

Total calls:

```text
n
```

Time:

```text
O(n)
```

Space (recursion stack):

```text
O(n)
```

---

### Fibonacci Recursion

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)
```

Tree looks like:

```text
            fib(5)
          /       \
      fib(4)     fib(3)
      /   \       /  \
```

Nodes grow exponentially.

Time:

```text
O(2ⁿ)
```

Space:

```text
O(n)
```

---

# Question 3: Merge Sort Complexity

Algorithm:

```text
Split
Split
Split
Merge
Merge
Merge
```

Example:

```text
[8,4,2,6]

→ [8,4] [2,6]

→ [8] [4] [2] [6]
```

Levels:

```text
log n
```

Work per level:

```text
n
```

Total:

```text
O(n log n)
```

Space:

```text
O(n)
```

### Summary

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |

---

# Question 4: Quick Sort Complexity

Pivot chosen:

```text
[4,2,8,1,6]
```

### Best Case

Balanced partitions:

```text
O(n log n)
```

### Average Case

```text
O(n log n)
```

### Worst Case

Already sorted array:

```python
[1,2,3,4,5]
```

Pivot = first element.

Partitions:

```text
1 and n-1
```

Time:

```text
O(n²)
```

### Space

```text
O(log n)
```

---

# Question 5: Hash Table Complexity

Python Dictionary:

```python
d = {}

d["name"] = "Nikita"
```

Uses hashing internally.

| Operation | Average | Worst |
| --------- | ------- | ----- |
| Insert    | O(1)    | O(n)  |
| Search    | O(1)    | O(n)  |
| Delete    | O(1)    | O(n)  |

### Why Worst Case O(n)?

If many keys generate the same hash value:

```text
Collision
```

Then Python may need to check many entries.

---

# Interview Tip

Memorize this table:

| Operation        | Complexity |
| ---------------- | ---------- |
| Array Access     | O(1)       |
| Linear Search    | O(n)       |
| Binary Search    | O(log n)   |
| HashMap Search   | O(1)       |
| Merge Sort       | O(n log n) |
| Quick Sort Avg   | O(n log n) |
| Quick Sort Worst | O(n²)      |
| BFS              | O(V+E)     |
| DFS              | O(V+E)     |
| Heap Insert      | O(log n)   |
| Heap Delete      | O(log n)   |

These are among the most frequently asked complexity questions in DSA interviews.


# two sum 

This is the famous **LeetCode 11: Container With Most Water** problem.

Let's solve it in two ways:

1. **Brute Force** - Check every possible pair.
2. **Optimized (Two Pointers)** - O(n) solution.

---

# 1. Brute Force Solution

### Idea

* Pick every pair of lines `(i, j)`.
* Calculate:

  * Width = `j - i`
  * Height = `min(height[i], height[j])`
  * Area = `width * height`
* Keep track of the maximum area.

### Code

```python
class Solution(object):
    def maxArea(self, height):
        n = len(height)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):

                width = j - i
                h = min(height[i], height[j])
                area = width * h

                max_area = max(max_area, area)

        return max_area
```

### Time Complexity

* Outer loop = O(n)
* Inner loop = O(n)

**Overall = O(n²)**

### Space Complexity

**O(1)**

---

# Dry Run

```
height = [1,8,6,2]
```

| i | j | Width | Min Height | Area | Max |
| - | - | ----- | ---------- | ---- | --- |
| 0 | 1 | 1     | 1          | 1    | 1   |
| 0 | 2 | 2     | 1          | 2    | 2   |
| 0 | 3 | 3     | 1          | 3    | 3   |
| 1 | 2 | 1     | 6          | 6    | 6   |
| 1 | 3 | 2     | 2          | 4    | 6   |
| 2 | 3 | 1     | 2          | 2    | 6   |

Answer = **6**

---

# Why Brute Force is Slow?

For every line, we're checking every other line.

If `n = 100000`

```
100000 × 100000
```

≈ **10 billion comparisons**, which is too slow.

---

# 2. Optimized Solution (Two Pointers)

## Observation

The area depends on

```
Area = Width × Min(height[left], height[right])
```

Initially, use the widest container.

```
left = 0
right = n-1
```

Then shrink the width intelligently.

---

## Important Logic

Suppose

```
left = 2
right = 8

height[left] = 4
height[right] = 9
```

Area

```
= min(4,9) × width
= 4 × width
```

The **smaller height (4)** is limiting the area.

Even if we move the taller line,

```
height[right] = 9
```

the minimum height will still be at most 4 unless the left height changes.

So moving the taller line cannot increase the area.

Therefore:

* Move the shorter line.
* Hope to find a taller line.

---

# Algorithm

```
left = 0
right = n-1

while left < right:

    area = min(height[left], height[right]) * (right-left)

    update answer

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
```

---

# Code

```python
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            width = right - left
            h = min(height[left], height[right])
            area = width * h

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

# Complete Dry Run

```
height = [1,8,6,2,5,4,8,3,7]
```

### Initial

```
L = 0 (1)
R = 8 (7)
```

Area

```
width = 8

min = 1

Area = 8
```

Max = 8

Move smaller

```
Left++
```

---

### Now

```
L = 1 (8)
R = 8 (7)
```

Area

```
width = 7

min = 7

Area = 49
```

Max = 49

Move smaller

```
Right--
```

---

### Now

```
L = 1 (8)
R = 7 (3)
```

Area

```
6 × 3 = 18
```

Move Right

---

### Now

```
L = 1 (8)
R = 6 (8)
```

Area

```
5 × 8 = 40
```

Move either one (both equal). Here, move Right.

---

### Now

```
L = 1 (8)
R = 5 (4)

Area = 4 × 4 = 16
```

Move Right.

---

### Now

```
L = 1 (8)
R = 4 (5)

Area = 3 × 5 = 15
```

Move Right.

---

### Now

```
L = 1 (8)
R = 3 (2)

Area = 2 × 2 = 4
```

Move Right.

---

### Now

```
L = 1 (8)
R = 2 (6)

Area = 1 × 6 = 6
```

Move Right.

Now

```
left == right
```

Stop.

Answer:

```
49
```

---

# Why Move the Smaller Height?

Suppose:

```
5 -------------------- 9
```

Area

```
Width × 5
```

If you move the taller line:

```
5 ------------- 8
```

The width decreases, but the limiting height is still 5 (or less), so the area cannot increase.

If instead you move the shorter line:

```
10 ---------------- 9
```

Now the limiting height becomes 9, and although the width is slightly smaller, the larger minimum height can produce a greater area.

This is why the two-pointer algorithm always moves the pointer at the **shorter line**.

---

## Complexity Comparison

| Approach     | Time      | Space    |
| ------------ | --------- | -------- |
| Brute Force  | **O(n²)** | **O(1)** |
| Two Pointers | **O(n)**  | **O(1)** |

The optimized two-pointer solution is the preferred approach for interviews because it reduces the time complexity from quadratic to linear while using constant extra space.




linkedlist
circular linked list 
reverse through stack 
circular linked list find
double pointer linked how is it work and its code
