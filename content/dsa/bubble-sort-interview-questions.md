# Bubble Sort Interview Questions (Beginner to Advanced)

## 1. What is Bubble Sort?

**Answer:**

Bubble Sort is a comparison-based sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.

After every pass, the largest (or smallest) element moves to its correct position.

Example:

```
5 3 8 4

Pass 1:
5 3 -> swap
3 5 8 4

8 4 -> swap
3 5 4 8

Largest element (8) reached the end.
```

---

## 2. Why is it called Bubble Sort?

Because the largest (or smallest) element **bubbles up** to the end of the array after each pass.

---

## 3. Write Bubble Sort in Python

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
```

---

## 4. Explain Bubble Sort step by step

Example

```
[5,1,4,2]
```

### Pass 1

```
5 1 -> swap

1 5 4 2

5 4 -> swap

1 4 5 2

5 2 -> swap

1 4 2 5
```

Largest = 5

---

### Pass 2

```
1 4 2 5

4 2 -> swap

1 2 4 5
```

Largest = 4

---

### Pass 3

```
Already Sorted
```

Result

```
1 2 4 5
```

---

# 5. Time Complexity

| Case    | Complexity       |
| ------- | ---------------- |
| Best    | O(n) (Optimized) |
| Average | O(n²)            |
| Worst   | O(n²)            |

---

# 6. Space Complexity

```
O(1)
```

It is an in-place sorting algorithm.

---

# 7. Is Bubble Sort Stable?

Yes.

Equal elements never change their relative order.

Example

```
5A 2 5B 1

After sorting

1 2 5A 5B
```

5A stays before 5B.

---

# 8. Is Bubble Sort In-place?

Yes.

It only uses one temporary variable while swapping.

---

# 9. Bubble Sort Optimization

If no swaps occur during a pass, the array is already sorted.

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

                swapped = True

        if not swapped:
            break

    return arr
```

---

# 10. Why is optimized Bubble Sort O(n) in the best case?

Example

```
1 2 3 4 5
```

Only one pass occurs.

No swaps.

Algorithm exits.

Hence

```
O(n)
```

---

# 11. Number of passes

For

```
n elements
```

Maximum passes

```
n-1
```

---

# 12. Number of comparisons

```
(n-1)+(n-2)+(n-3)+...+1

= n(n-1)/2
```

Complexity

```
O(n²)
```

---

# 13. Number of swaps

Worst Case

```
n(n-1)/2
```

Best Case

```
0
```

---

# 14. Dry Run Question

Sort

```
4 3 2 1
```

Pass 1

```
3 4 2 1

3 2 4 1

3 2 1 4
```

Pass 2

```
2 3 1 4

2 1 3 4
```

Pass 3

```
1 2 3 4
```

---

# 15. Bubble Sort for Descending Order

```python
def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n-i-1):

            if arr[j] < arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
```

---

# 16. Bubble Sort using Recursion

```python
def bubble(arr, n):

    if n == 1:
        return

    for i in range(n-1):

        if arr[i] > arr[i+1]:

            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubble(arr, n-1)
```

---

# 17. Bubble Sort using While Loop

```python
def bubble(arr):

    n = len(arr)

    while n > 1:

        i = 0

        while i < n-1:

            if arr[i] > arr[i+1]:

                arr[i], arr[i+1] = arr[i+1], arr[i]

            i += 1

        n -= 1

    return arr
```

---

# 18. Advantages

* Very easy to implement
* Stable
* In-place
* Good for teaching sorting concepts
* Can detect already sorted arrays (optimized version)

---

# 19. Disadvantages

* Very slow
* O(n²)
* Not suitable for large datasets
* Performs many unnecessary comparisons

---

# 20. Bubble Sort vs Selection Sort

| Feature   | Bubble           | Selection                    |
| --------- | ---------------- | ---------------------------- |
| Stable    | Yes              | No (standard implementation) |
| Swaps     | Many             | Few                          |
| Time      | O(n²)            | O(n²)                        |
| Best Case | O(n) (optimized) | O(n²)                        |
| Space     | O(1)             | O(1)                         |

---

# 21. Bubble Sort vs Insertion Sort

| Bubble                  | Insertion                        |
| ----------------------- | -------------------------------- |
| Swaps adjacent elements | Inserts element into sorted part |
| O(n²)                   | O(n²)                            |
| Best O(n)               | Best O(n)                        |
| More swaps              | Fewer swaps                      |
| Slower                  | Usually faster                   |

---

# 22. Bubble Sort vs Merge Sort

| Bubble       | Merge                   |
| ------------ | ----------------------- |
| O(n²)        | O(n log n)              |
| O(1) Space   | O(n) Space              |
| In-place     | Not in-place (standard) |
| Stable       | Stable                  |
| Small arrays | Large arrays            |

---

# 23. Bubble Sort vs Quick Sort

| Bubble    | Quick                 |
| --------- | --------------------- |
| O(n²)     | Average O(n log n)    |
| Stable    | Not stable (standard) |
| Easy      | Complex               |
| Very Slow | Very Fast             |

---

# 24. Can Bubble Sort sort linked lists?

Yes.

However, **Insertion Sort** or **Merge Sort** is usually preferred for linked lists because Bubble Sort requires many comparisons and swaps.

---

# 25. Can Bubble Sort sort strings?

Yes.

Example

```python
arr = list("bubble")

bubble_sort(arr)

print("".join(arr))
```

Output

```
bbbelu
```

---

# 26. Can Bubble Sort sort objects?

Yes.

Example

```python
students = [
    ("John", 90),
    ("Alice", 70),
    ("Bob", 85)
]

n = len(students)

for i in range(n):
    for j in range(n-i-1):
        if students[j][1] > students[j+1][1]:
            students[j], students[j+1] = students[j+1], students[j]

print(students)
```

---

# 27. Why isn't Bubble Sort used in real applications?

Because its **O(n²)** time complexity makes it inefficient for large datasets. Modern libraries use algorithms like **Timsort** (Python), Merge Sort, Quick Sort, or Heap Sort, which are significantly faster.

---

# 28. Common Coding Interview Variations

1. Sort an array using Bubble Sort.
2. Count the total number of swaps performed.
3. Stop early if the array is already sorted.
4. Sort in descending order.
5. Sort a list of strings.
6. Sort a list of objects based on a key.
7. Find the k-th largest element using Bubble Sort.
8. Bubble Sort using recursion.
9. Bubble Sort using only one loop (with modified logic).
10. Explain Bubble Sort with a dry run on paper.

---

# 29. Frequently Asked Viva Questions

* What is Bubble Sort?
* Why is it called Bubble Sort?
* Is Bubble Sort stable?
* Is Bubble Sort adaptive?
* Is Bubble Sort in-place?
* What is its best-case complexity?
* What is its worst-case complexity?
* How can Bubble Sort be optimized?
* Why is Bubble Sort rarely used in production?
* Which sorting algorithms are generally preferred over Bubble Sort and why?

---

## Interview Tip

In coding interviews, after implementing the basic Bubble Sort, proactively mention:

* It is **stable** and **in-place**.
* The standard implementation has **O(n²)** average and worst-case time complexity.
* An optimized version uses a `swapped` flag to achieve **O(n)** best-case performance on already sorted arrays.
* It is mainly used for educational purposes; practical applications typically favor algorithms like Merge Sort, Quick Sort, or Timsort.

These are two of the most important properties of sorting algorithms, and interviewers ask about them very frequently.

---

# 1. What is an In-Place Sorting Algorithm?

An **in-place** sorting algorithm sorts the data **without requiring significant extra memory**. It modifies the original array directly.

* It uses only a **constant amount of extra space**, typically `O(1)`.
* The original array is rearranged instead of creating a new one.

### Example

Suppose you have:

```text
arr = [5, 3, 8, 2]
```

Bubble Sort swaps elements directly inside the same array.

```text
[5,3,8,2]

↓

[3,5,8,2]

↓

[3,5,2,8]

↓

[2,3,5,8]
```

The original array becomes sorted.

No second array is created.

Memory usage:

```text
Extra Space = O(1)
```

That's why Bubble Sort is **in-place**.

---

### Example of NOT In-Place

Consider Merge Sort.

Original array:

```text
[5,3,8,2]
```

Merge Sort divides it:

```text
[5,3]    [8,2]
```

Then it creates temporary arrays:

```text
Left = [3,5]

Right = [2,8]
```

Finally:

```text
Result = [2,3,5,8]
```

Since additional arrays are created, Merge Sort is **not in-place** (in its standard implementation).

---

## Memory Comparison

| Algorithm      | Extra Space | In-Place? |
| -------------- | ----------: | :-------: |
| Bubble Sort    |        O(1) |   ✅ Yes   |
| Selection Sort |        O(1) |   ✅ Yes   |
| Insertion Sort |        O(1) |   ✅ Yes   |
| Merge Sort     |        O(n) |    ❌ No   |
| Counting Sort  |      O(n+k) |    ❌ No   |

---

# 2. What is a Stable Sorting Algorithm?

A sorting algorithm is **stable** if **equal elements keep their original relative order** after sorting.

The values are equal, but we label them so we can track them.

Suppose we have employees sorted by age:

```text
John (25)
Alice (20)
Bob (25)
David (30)
```

Notice:

```text
John (25)
↓
Bob (25)
```

John appears before Bob.

Now sort by age.

A **stable** algorithm produces:

```text
Alice (20)

John (25)

Bob (25)

David (30)
```

John is still before Bob.

The order of equal elements did **not** change.

---

### Unstable Example

If the result becomes:

```text
Alice (20)

Bob (25)

John (25)

David (30)
```

Both have age 25, but their relative order changed.

This algorithm is **not stable**.

---

## Another Example

Original array:

```text
[(A,5), (B,2), (C,5), (D,1)]
```

Sorting by the number gives:

```text
[(D,1), (B,2), (A,5), (C,5)]
```

A (5) is still before C (5).

✅ Stable

If the result were:

```text
[(D,1), (B,2), (C,5), (A,5)]
```

❌ Unstable

---

# Why is Bubble Sort Stable?

Bubble Sort swaps **only when the left element is greater than the right element**.

```python
if arr[j] > arr[j + 1]:
    arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

Notice it uses:

```python
>
```

not

```python
>=
```

If two adjacent elements are equal:

```text
5A 5B
```

Then:

```python
5A > 5B
```

is **False**, so no swap happens.

Therefore:

```text
Before:
5A 5B

After:
5A 5B
```

Their order stays the same, making Bubble Sort **stable**.

---

# Quick Interview Trick

Interviewer: **Is Bubble Sort stable?**

You can answer:

> Yes. Bubble Sort is stable because it swaps elements only when the left element is strictly greater than the right one. Equal elements are never swapped, so their original relative order is preserved.

---

Interviewer: **Is Bubble Sort in-place?**

You can answer:

> Yes. Bubble Sort is an in-place sorting algorithm because it sorts the array by swapping elements within the original array and uses only a constant amount of extra memory, i.e., **O(1)** auxiliary space.

---

## Easy way to remember

| Property     | Meaning                                                          | Bubble Sort |
| ------------ | ---------------------------------------------------------------- | :---------: |
| **In-place** | Sorts inside the original array without allocating another array |    ✅ Yes    |
| **Stable**   | Equal elements remain in the same relative order after sorting   |    ✅ Yes    |

A simple mnemonic is:

* **In-place = "Where is the data stored?"** → In the **same array**.
* **Stable = "What happens to equal elements?"** → They **keep their original order**.
