# Sorting Algorithms in Python — Complete Interview Prep Guide (with Solutions)

Every algorithm below includes **iterative + recursive code**, complexity analysis, and **Basic + Advanced interview questions with full written solutions**. The final section gives **working code solutions** to 18 classic Google-style sorting problems.

---

## Table of Contents

1. [Bubble Sort](#1-bubble-sort)
2. [Selection Sort](#2-selection-sort)
3. [Insertion Sort](#3-insertion-sort)
4. [Merge Sort](#4-merge-sort)
5. [Quick Sort](#5-quick-sort)
6. [Heap Sort](#6-heap-sort)
7. [Counting Sort](#7-counting-sort)
8. [Radix Sort](#8-radix-sort)
9. [Bucket Sort](#9-bucket-sort)
10. [Shell Sort](#10-shell-sort)
11. [Complexity Cheat Sheet](#complexity-cheat-sheet)
12. [When to Use Which Sort](#when-to-use-which-sort)
13. [General Questions — Basic & Advanced (with Answers)](#general-questions--basic--advanced-with-answers)
14. [Coding Problems with Full Solutions](#coding-problems-with-full-solutions)
15. [4-Week Prep Plan](#suggested-preparation-strategy)

---

## 1. Bubble Sort

**Definition:** Repeatedly steps through the array, compares each pair of adjacent elements, and swaps them if they're in the wrong order. This "bubbles" the largest unsorted element to its correct position at the end on every pass.

**When to use it:** Almost never in production. Only useful for teaching sorting concepts, or for tiny (few elements) or already-nearly-sorted datasets where its early-exit optimization gives near O(n) performance.

### Iterative
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

### Recursive
```python
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    if not swapped:
        return arr
    return bubble_sort_recursive(arr, n - 1)
```

**Time:** O(n²) worst/avg, O(n) best | **Space:** O(1) iterative, O(n) recursive stack | **Stable:** Yes | **In-place:** Yes

### Basic Questions & Answers

**Q1. Why is Bubble Sort rarely used in production?**
A. It performs O(n²) comparisons and swaps even for moderately sized inputs, making it far slower than O(n log n) algorithms like Merge/Quick Sort. It's used mainly for teaching and for tiny, nearly-sorted datasets.

**Q2. How does the `swapped` flag change best-case complexity?**
A. Without it, Bubble Sort always runs all n-1 passes → O(n²) even on sorted input. With the flag, if a full pass makes zero swaps the array is already sorted, so the loop exits early → best case becomes O(n) on an already-sorted array.

**Q3. Is Bubble Sort stable? Prove it.**
A. Yes — it only swaps adjacent elements when `arr[j] > arr[j+1]` (strictly greater), so equal elements are never swapped, preserving their original relative order. Example: `[(3,'a'), (3,'b')]` → comparison `3 > 3` is False, no swap, order preserved.

**Q4. Modify Bubble Sort to sort in descending order.**
A.
```python
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:      # flipped comparison
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Advanced Questions & Answers

**Q5. Can Bubble Sort be parallelized? Explain Odd-Even Transposition Sort.**
A. Standard Bubble Sort is inherently sequential (each swap depends on the previous comparison in the same pass). Odd-Even Transposition Sort parallelizes it: in odd phases compare-swap pairs (1,2),(3,4),(5,6)...; in even phases compare-swap pairs (2,3),(4,5)... All comparisons within a phase are independent and can run in parallel. It still takes O(n) phases, giving O(n) parallel time with O(n) processors vs O(n²) sequential.
```python
def odd_even_sort(arr):
    n = len(arr)
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(1, n - 1, 2):      # odd phase
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False
        for i in range(0, n - 1, 2):      # even phase
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False
    return arr
```

**Q6. What is the exact number of comparisons and swaps in the worst case, and how do you derive it?**
A. Worst case (reverse-sorted input): total comparisons = (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n²). Every comparison also causes a swap in the worst case, so swaps are also O(n²). This is derived via the standard arithmetic series sum for nested loops where the inner loop shrinks by 1 each outer iteration.

**Q7. How does recursive Bubble Sort's space complexity compare to iterative, and why does it matter at scale?**
A. Iterative uses O(1) auxiliary space. Recursive uses O(n) call-stack space because each recursive call adds a stack frame until the base case. For large n (e.g., 10⁵+), this risks a stack overflow in Python (default recursion limit ~1000), so recursive Bubble Sort is impractical beyond small inputs — an important trade-off to mention when asked "would you ever use the recursive version?"

---

## 2. Selection Sort

**Definition:** Divides the array into a sorted and unsorted region. On each pass, it finds the minimum element in the unsorted region and swaps it into the next position of the sorted region.

**When to use it:** When the cost of writing/swapping is very high (e.g., flash memory, EEPROM) since it makes only O(n) swaps total, far fewer than Bubble or Insertion Sort. Also fine for very small arrays where simplicity matters more than speed.

### Iterative
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### Recursive
```python
def selection_sort_recursive(arr, start=0):
    n = len(arr)
    if start >= n - 1:
        return arr
    min_idx = start
    for j in range(start + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    return selection_sort_recursive(arr, start + 1)
```

**Time:** O(n²) always | **Space:** O(1) | **Stable:** No | **In-place:** Yes

### Basic Questions & Answers

**Q1. Why does Selection Sort always run in O(n²), unlike Bubble Sort's O(n) best case?**
A. Selection Sort scans the entire remaining unsorted sub-array to find the minimum on every single pass, regardless of whether the array is already sorted. There's no early-exit condition, so it always performs (n-1)+(n-2)+...+1 = O(n²) comparisons.

**Q2. Why is standard Selection Sort not stable? Give an example.**
A. It swaps the found minimum directly into position i, which can jump it past equal elements. Example: `[(4,'a'), (2,'b'), (4,'c')]` sorting by first value — the second `4` (with tag 'c') gets swapped to the front ahead of `(4,'a')`, breaking original relative order.

**Q3. How many swaps does Selection Sort perform in total?**
A. Exactly n-1 swaps in the worst case (one swap per outer iteration, and the last element needs none), unlike Bubble/Insertion which can perform up to O(n²) swaps. This is why Selection Sort is preferred when write operations are expensive.

### Advanced Questions & Answers

**Q4. How would you modify Selection Sort to be stable?**
A. Instead of swapping the minimum into place, **shift** all elements between the min's original position and the target position one step right, then insert the minimum. This avoids jumping the minimum past equal elements — but costs more writes (O(n) shifts per pass instead of O(1) swap), degrading the "few writes" advantage.
```python
def stable_selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        key = arr[min_idx]
        while min_idx > i:                 # shift instead of swap
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = key
    return arr
```

**Q5. Why does minimizing writes matter, and where is this relevant in real systems?**
A. Selection Sort makes O(n) writes vs O(n²) for Bubble/Insertion in the worst case. This matters for storage media with limited write endurance (flash memory/SSDs, EEPROM) or where writes are far more expensive than reads (e.g., writing to slow remote storage). Selection Sort trades comparison count for write count.

**Q6. Implement "Double-Ended Selection Sort" that finds both min and max per pass to halve the number of outer iterations.**
A.
```python
def double_selection_sort(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        min_idx, max_idx = left, left
        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i
        arr[left], arr[min_idx] = arr[min_idx], arr[left]
        # if max was at 'left', it just moved to min_idx
        if max_idx == left:
            max_idx = min_idx
        arr[right], arr[max_idx] = arr[max_idx], arr[right]
        left += 1
        right -= 1
    return arr
```
This still does O(n²) comparisons overall (same order), but halves the number of outer-loop passes — a good discussion point on constant-factor optimization not changing Big-O.

---

## 3. Insertion Sort

**Definition:** Builds the sorted array one element at a time by taking each new element and inserting it into its correct position among the already-sorted elements to its left, shifting larger elements right to make room.

**When to use it:** Small arrays, nearly-sorted data, or as the base case inside hybrid algorithms (Timsort, Introsort use it for small sub-arrays/runs). Also ideal for online sorting where data arrives one element at a time, and for linked lists where insertion is O(1).

### Iterative
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### Recursive
```python
def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    insertion_sort_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    return arr
```

**Time:** O(n²) worst/avg, O(n) best | **Space:** O(1) iterative | **Stable:** Yes | **In-place:** Yes

### Basic Questions & Answers

**Q1. Why is Insertion Sort good for small or nearly-sorted arrays?**
A. Its running time is proportional to the number of *inversions* in the array. For a nearly-sorted array, each element needs only a few shifts to reach its correct place, so actual work approaches O(n) rather than O(n²). This is why Timsort and Introsort fall back to Insertion Sort for small partitions (typically <16-64 elements) — overhead of Merge/Quick Sort's recursion isn't worth it at that scale.

**Q2. Trace Insertion Sort on `[5, 2, 4, 6, 1, 3]`.**
A.
```
[5, 2, 4, 6, 1, 3]
[2, 5, 4, 6, 1, 3]
[2, 4, 5, 6, 1, 3]
[2, 4, 5, 6, 1, 3]
[1, 2, 4, 5, 6, 3]
[1, 2, 3, 4, 5, 6]
```

**Q3. Is Insertion Sort stable? Why?**
A. Yes. The inner `while` loop only shifts elements strictly greater than `key` (`arr[j] > key`), so equal elements are never moved past each other.

### Advanced Questions & Answers

**Q4. How does Binary Insertion Sort reduce comparisons, and does it change overall time complexity?**
A. Instead of a linear scan to find the insertion point, use binary search — reducing comparisons from O(n) to O(log n) per element. However, **shifting** elements to make room is still O(n) per insertion (array shifting can't be sped up by binary search), so total time remains O(n²) in the worst case — only the *comparison count* improves to O(n log n), not the overall time complexity.
```python
import bisect

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = bisect.bisect_left(arr, key, 0, i)
        arr[pos + 1:i + 1] = arr[pos:i]
        arr[pos] = key
    return arr
```

**Q5. Why is Insertion Sort more efficient on a linked list than Selection Sort?**
A. On a linked list, insertion (splicing a node into place) is O(1) once the position is found, since there's no shifting — you just relink pointers. Selection Sort still needs to scan for the minimum each pass (O(n)) and, more importantly, gains nothing from the list structure since swapping isn't cheaper. Insertion Sort exploits O(1) insertion, making it a better fit for linked structures.

**Q6. Why does Timsort (Python's `sorted()`) use Insertion Sort internally?**
A. Timsort splits the array into "runs." For runs smaller than a threshold (`MIN_RUN`, typically 32-64), it uses Binary Insertion Sort because: (1) Insertion Sort has very low constant-factor overhead and good cache locality for small arrays, (2) it's stable, and (3) it performs efficiently on the small, often nearly-ordered runs typical of real-world data. Then Timsort merges these sorted runs using an optimized Merge Sort.

---

## 4. Merge Sort

**Definition:** A divide-and-conquer algorithm that recursively splits the array in half until single elements remain, then merges the sorted halves back together in order.

**When to use it:** When you need **guaranteed** O(n log n) performance regardless of input, when **stability** is required (e.g., multi-key sorting), when sorting **linked lists** (no random access needed, O(1) extra space for merging), or for **external sorting** of data too large to fit in memory (k-way merge of sorted chunks).

### Recursive (standard)
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Iterative (bottom-up)
```python
def merge_sort_iterative(arr):
    n = len(arr)
    width = 1
    arr = arr[:]
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + len(left) + len(right)] = merge(left, right)
        width *= 2
    return arr
```

**Time:** O(n log n) always | **Space:** O(n) | **Stable:** Yes | **In-place:** No

### Basic Questions & Answers

**Q1. Derive Merge Sort's time complexity from its recurrence.**
A. T(n) = 2T(n/2) + O(n). By the Master Theorem (a=2, b=2, f(n)=O(n)): since f(n) = Θ(n^log_b(a)) = Θ(n¹), this is Case 2, giving T(n) = Θ(n log n). Intuitively: log n levels of recursion, each level does O(n) total work to merge.

**Q2. Why is Merge Sort O(n log n) in the best, average, AND worst case (unlike Quick Sort)?**
A. Because the split is always exactly in half regardless of input order (no dependency on data values), and merging two sorted halves is always O(n) regardless of their contents. There's no data-dependent behavior that could degrade performance.

**Q3. Why does Merge Sort need O(n) extra space?**
A. The merge step needs a temporary array to hold combined results, because merging in-place while reading from both halves would overwrite elements not yet processed. Some in-place merge algorithms exist but they either sacrifice O(n log n) time or add significant complexity/constant factors.

### Advanced Questions & Answers

**Q4. Why is Merge Sort preferred for linked lists over arrays?**
A. Two reasons: (1) Merge Sort's merge step just needs sequential access + pointer manipulation — no random access needed, which fits linked lists perfectly (unlike Quick Sort, which needs random access for partitioning). (2) Merging linked lists needs **no extra space** (just relinking nodes) — eliminating the usual O(n) space downside on arrays.
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = merge_sort_list(head)
    right = merge_sort_list(mid)
    return merge_lists(left, right)

def merge_lists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

**Q5. How would you merge k sorted arrays? Derive complexity.**
A. Use a min-heap of size k holding (value, array_index, element_index). Pop the min, push its successor from the same array. Total elements N across all arrays → each of N pops/pushes costs O(log k) → **O(N log k)** total, better than repeatedly merging pairs (O(N log k) is optimal; naive pairwise merging is also O(N log k) but with worse constants). See full code in the Coding Problems section.

**Q6. How is external sorting (data too large for RAM) related to Merge Sort?**
A. External Merge Sort: (1) split data into chunks that fit in memory, sort each chunk in-memory (e.g., with Quick/Merge Sort) and write to disk as sorted "runs," (2) perform a k-way merge of these runs reading only small buffered portions of each into memory at a time, using a min-heap to pick the next smallest element. This is exactly how large-scale systems (databases, `sort` command with `--buffer-size`, distributed sort in MapReduce) sort data far bigger than available RAM.

**Q7. Count inversions in an array using modified Merge Sort. What's an inversion and why does Merge Sort suit this?**
A. An inversion is a pair (i, j) where i < j but arr[i] > arr[j] — a measure of "how unsorted" an array is. During the merge step, whenever we take an element from the right half before exhausting the left half, every remaining element in the left half forms an inversion with it — so we can count these for free during merging.
```python
def count_inversions(arr):
    def sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_left = sort_count(a[:mid])
        right, inv_right = sort_count(a[mid:])
        merged, inv_split = merge_count(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge_count(left, right):
        result, i, j, inv = [], 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
                inv += len(left) - i        # key line: count inversions
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv

    _, total_inversions = sort_count(arr)
    return total_inversions
```

---

## 5. Quick Sort

**Definition:** A divide-and-conquer algorithm that picks a "pivot" element, partitions the array so smaller elements go left and larger go right of the pivot, then recursively sorts each partition.

**When to use it:** The **default general-purpose choice** for in-memory array sorting when average-case speed matters most — it has excellent cache locality, sorts in-place (O(log n) space), and is typically the fastest in practice. Avoid it when worst-case guarantees are required, stability is needed, or input could be adversarially crafted (use randomized pivots to mitigate).

### Recursive (Lomuto partition)
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition_lomuto(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition_lomuto(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### Recursive (Hoare partition)
```python
def quick_sort_hoare(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition_hoare(arr, low, high)
        quick_sort_hoare(arr, low, pi)
        quick_sort_hoare(arr, pi + 1, high)
    return arr

def partition_hoare(arr, low, high):
    pivot = arr[low]
    i, j = low - 1, high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
```

### Iterative (explicit stack)
```python
def quick_sort_iterative(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition_lomuto(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    return arr
```

### Randomized pivot
```python
import random

def quick_sort_randomized(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
        pi = partition_lomuto(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)
    return arr
```

**Time:** O(n log n) avg, O(n²) worst | **Space:** O(log n) avg stack | **Stable:** No | **In-place:** Yes

### Basic Questions & Answers

**Q1. Why does Quick Sort degrade to O(n²) on sorted input with a naive (e.g., last-element) pivot?**
A. If the array is already sorted and you always pick the last element as pivot, every partition splits the array into one empty side and one side of size n-1 (since the pivot is always the max or min of the remaining range). This gives the recurrence T(n) = T(n-1) + O(n), which sums to O(n²) — essentially degenerating into Selection-Sort-like behavior.

**Q2. How does randomized/median-of-three pivot selection fix this?**
A. Randomly selecting the pivot (or using the median of first/middle/last elements) makes worst-case behavior extremely unlikely for any *fixed* input, because the adversarial input that breaks one particular pivot rule won't reliably break a randomly chosen one. Expected time becomes O(n log n) regardless of input order.

**Q3. Compare Lomuto vs Hoare partition schemes.**
A. Lomuto: simpler, always uses the last element as pivot, does more swaps on average, and pivot lands in its final sorted position. Hoare: uses first element as pivot, does about 3x fewer swaps, but the returned index isn't guaranteed to be the pivot's final position (so recursive calls must be `(low, pi)` and `(pi+1, high)`, not `pi-1`). Hoare is generally more efficient in practice.

### Advanced Questions & Answers

**Q4. Why is Quick Sort not stable? Can you make it stable, and at what cost?**
A. Partitioning swaps elements across arbitrary distances based on pivot comparison, which can reorder equal elements relative to each other. You *can* make it stable by using extra space (essentially degrading into something like a stable partition using auxiliary arrays — similar to Merge Sort's approach), but this sacrifices Quick Sort's main advantage: O(log n) space, in-place operation. In practice, if you need stability, you use Merge Sort instead.

**Q5. Why is Quick Sort generally faster in practice than Merge Sort despite the same average complexity?**
A. (1) **Cache locality**: Quick Sort operates in-place on contiguous memory with good locality of reference; Merge Sort allocates new arrays, causing more cache misses and memory allocation overhead. (2) **Lower constant factors**: no extra array copying/merging step. (3) In-place partitioning avoids the O(n) auxiliary space allocation that Merge Sort requires on every merge.

**Q6. How would you find the kth smallest/largest element without fully sorting? Derive Quickselect's complexity.**
A. Quickselect uses Quick Sort's partition step but recurses into only *one* side (the side containing the target index) instead of both. Recurrence: T(n) = T(n/2) + O(n) on average (partition splits roughly evenly) → by the Master Theorem this resolves to **O(n)** average time (geometric series: n + n/2 + n/4 + ... = 2n = O(n)). Worst case is still O(n²) with bad pivots, fixable with randomization or median-of-medians (guarantees O(n) worst case).
```python
import random

def quickselect(arr, k):
    """Returns the kth smallest element (0-indexed)."""
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
```

**Q7. What is 3-way Quick Sort (Dutch National Flag partitioning) and when is it useful?**
A. Standard 2-way partitioning wastes time when there are many duplicate keys, since equal elements still get compared and shuffled repeatedly across recursive calls. 3-way partitioning splits the array into **three** regions in one pass: `< pivot`, `== pivot`, `> pivot`, and only recurses on the less-than and greater-than regions. This turns O(n log n) with many duplicates into close to O(n) since the "equal" partition never gets recursed into again.
```python
def quick_sort_3way(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low >= high:
        return arr
    lt, gt = low, high
    pivot = arr[low]
    i = low
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1; i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    quick_sort_3way(arr, low, lt - 1)
    quick_sort_3way(arr, gt + 1, high)
    return arr
```

**Q8. How do you limit stack usage to O(log n) even in the worst case (tail-call style optimization)?**
A. After partitioning, recurse into the **smaller** partition first, then use a loop (tail-call elimination) to handle the larger partition instead of a second recursive call. This bounds the recursion depth to O(log n) because you only ever "grow the stack" for the smaller half.
```python
def quick_sort_bounded_stack(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    while low < high:
        pi = partition_lomuto(arr, low, high)
        if pi - low < high - pi:            # left side smaller
            quick_sort_bounded_stack(arr, low, pi - 1)
            low = pi + 1                    # loop instead of recursing right
        else:
            quick_sort_bounded_stack(arr, pi + 1, high)
            high = pi - 1
    return arr
```

---

## 6. Heap Sort

**Definition:** Builds a max-heap from the array, then repeatedly swaps the root (largest element) with the last unsorted element and re-heapifies the reduced heap, placing elements into sorted order from the end.

**When to use it:** When you need guaranteed O(n log n) in the **worst case** with strictly O(1) extra space — good for memory-constrained or real-time systems where Quick Sort's worst case is unacceptable. Also the natural choice for "find top K elements" problems and implementing priority queues.

### Standard (recursive heapify)
```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### Fully iterative heapify
```python
def heapify_iterative(arr, n, i):
    while True:
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
```

**Time:** O(n log n) always | **Space:** O(1) | **Stable:** No | **In-place:** Yes

### Basic Questions & Answers

**Q1. Why does building a heap take O(n), not O(n log n)?**
A. Although each `heapify` call can take up to O(log n), most nodes are near the bottom of the tree where heapify does very little work. Summing the work across all levels: Σ (n / 2^(h+1)) · h for h = 0 to log n converges to O(n), not O(n log n) — this is a classic amortized analysis result (geometric series weighted by height).

**Q2. Why is Heap Sort not stable?**
A. The heapify/sift-down process swaps elements across non-adjacent positions based purely on value comparisons, with no mechanism to preserve original order among equal elements — equal keys can easily get reordered during the heap restructuring.

**Q3. Trace building a max-heap from `[4, 10, 3, 5, 1]`.**
A. Starting heapify from index `n//2 - 1 = 1` down to 0:
- i=1 (value 10): children are 5,1 — 10 is already largest, no change.
- i=0 (value 4): children are 10,3 — 10 is largest, swap → `[10, 4, 3, 5, 1]`; recurse at index 1 (value 4 now), children 5,1 — 5 is largest, swap → `[10, 5, 3, 4, 1]`.
Final max-heap: `[10, 5, 3, 4, 1]`.

### Advanced Questions & Answers

**Q4. Compare Heap Sort vs Quick Sort — when would you pick Heap Sort?**
A. Heap Sort guarantees O(n log n) in **all** cases with O(1) extra space, unlike Quick Sort's O(n²) worst case. Pick Heap Sort when: (1) worst-case time guarantees are critical (e.g., real-time systems, security-sensitive contexts where an adversary might craft worst-case input), (2) memory is extremely constrained (embedded systems), even though in typical practice Quick Sort is faster due to better cache locality.

**Q5. How is Heap Sort used to solve "find top K elements" problems efficiently?**
A. Instead of fully sorting all n elements (O(n log n)), maintain a min-heap of size k while streaming through the array: push each element, and if heap size exceeds k, pop the minimum. This keeps only the k largest elements seen so far. Total complexity: **O(n log k)**, much better than O(n log n) when k << n.
```python
import heapq

def top_k_elements(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap   # contains the k largest elements
```

**Q6. Implement a priority queue using a heap and explain its relationship to Heap Sort.**
A. A binary heap directly *is* the data structure behind an efficient priority queue: `insert` is O(log n) (sift-up), `extract-min/max` is O(log n) (sift-down after replacing root with last element). Heap Sort is essentially: build a max-heap (like a priority queue with all elements inserted), then repeatedly extract the max and place it at the end — i.e., Heap Sort = build a priority queue + repeated `extract-max`.
```python
import heapq

class MinPriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self, item):
        heapq.heappush(self.heap, item)
    def pop(self):
        return heapq.heappop(self.heap)
    def peek(self):
        return self.heap[0]
```

**Q7. How would you merge k sorted lists using a min-heap? Complexity?**
A. Push the first element of each of the k lists into a min-heap (tagged with list index). Repeatedly pop the smallest, add it to the result, and push the next element from the same source list. With N total elements across all lists, each of the N heap operations costs O(log k) → total **O(N log k)**. (Full code provided in the Coding Problems section — "Merge K Sorted Lists.")

---

## 7. Counting Sort

**Definition:** A non-comparison sort that counts the occurrences of each distinct value, then uses those counts (via prefix sums) to place each element directly into its correct output position.

**When to use it:** When sorting **integers (or discrete keys) within a small, known range** — e.g., ages 0-120, exam scores 0-100, grades. It's blazing fast (O(n+k)) but wastes memory/time if the range k is much larger than n.

### Iterative
```python
def counting_sort(arr):
    if not arr:
        return arr
    max_val, min_val = max(arr), min(arr)
    range_size = max_val - min_val + 1
    count = [0] * range_size
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1
    for i in range(1, range_size):
        count[i] += count[i - 1]
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    return output
```

**Time:** O(n + k) | **Space:** O(n + k) | **Stable:** Yes | **In-place:** No

### Basic Questions & Answers

**Q1. Why is Counting Sort not comparison-based, and how does that let it beat O(n log n)?**
A. It never compares two elements to each other — instead it directly counts occurrences of each value and uses that count to compute final positions via prefix sums. The Ω(n log n) lower bound only applies to algorithms that sort purely by pairwise comparisons (proven via decision-tree argument over n! permutations); Counting Sort sidesteps this entirely by exploiting the fact that keys are bounded integers.

**Q2. When does Counting Sort become inefficient?**
A. When the range of values k is much larger than n (e.g., sorting 100 numbers where values range from 0 to 10 billion) — then O(n+k) approaches O(k), which can be far worse than O(n log n). It's ideal when k = O(n).

### Advanced Questions & Answers

**Q3. Why must you iterate in reverse during output construction to preserve stability?**
A. The prefix-sum count array gives the *last* valid position for each value. Placing elements in original (forward) order would place the *last* occurrence of a value first in that slot and then decrement — causing later occurrences to appear before earlier ones in the output, breaking stability. Iterating in reverse ensures the *last* original occurrence of a value goes into the *last* available slot for that value, and earlier occurrences correctly land in earlier slots.

**Q4. How is Counting Sort used as a subroutine inside Radix Sort?**
A. Radix Sort applies Counting Sort repeatedly, once per digit position (from least significant to most significant), using the digit (0-9) as the "key" instead of the full number. Since Counting Sort is stable, sorting by each digit in turn while preserving order from the previous pass correctly builds up the full sorted order across all digits — this is the theoretical justification for why LSD Radix Sort works at all.

**Q5. Given ages 0-120 for a million people, why is Counting Sort ideal, and how would you optimize memory?**
A. n = 1,000,000, k = 121 → O(n + k) ≈ O(n), extremely fast, far better than O(n log n) comparison sorts. Memory optimization: since k is tiny and fixed, you don't even need the `output` array — you can directly reconstruct the sorted array from the count array by writing `count[v]` copies of each value v in order (skipping the prefix-sum/stable-output machinery entirely if stability isn't required), reducing to O(k) extra space instead of O(n+k).

---

## 8. Radix Sort

**Definition:** A non-comparison sort that sorts integers (or fixed-width keys like strings) digit by digit — either from least-significant to most-significant (LSD) or the reverse (MSD) — using a stable sort (typically Counting Sort) at each digit position.

**When to use it:** Sorting large volumes of **fixed-width keys** — integers with a bounded number of digits, IP addresses, fixed-length strings, hashes. It beats comparison sorts when the number of digits d is small relative to log n. Poor fit for floating-point numbers or unbounded-length keys.

### LSD Iterative
```python
def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    for i in range(n):
        arr[i] = output[i]
```

### MSD Recursive
```python
def radix_sort_msd(arr, digit_pos=None):
    if digit_pos is None:
        max_val = max(arr) if arr else 0
        digit_pos = len(str(max_val)) - 1
    if digit_pos < 0 or len(arr) <= 1:
        return arr
    buckets = [[] for _ in range(10)]
    for num in arr:
        d = (num // (10 ** digit_pos)) % 10
        buckets[d].append(num)
    result = []
    for bucket in buckets:
        result.extend(radix_sort_msd(bucket, digit_pos - 1))
    return result
```

**Time:** O(d(n+k)) | **Space:** O(n+k) | **Stable:** Yes | **In-place:** No

### Basic Questions & Answers

**Q1. Why does Radix Sort achieve O(n) effective time — doesn't that violate the comparison-sort lower bound?**
A. No violation — Radix Sort is non-comparison-based, like Counting Sort. Its true complexity is O(d · (n + k)) where d is the number of digits and k is the digit base (10). For fixed-width integers, d is treated as a constant, so it *appears* linear — but if d grows with n (e.g., sorting numbers with up to n digits), the true complexity is no longer O(n).

**Q2. How would you adapt Radix Sort to sort strings?**
A. Treat each string as a sequence of "digits" (characters). Pad shorter strings conceptually with a sentinel value smaller than any character, then apply Counting Sort character-position by character-position, either LSD-style from the last character (all strings padded to the max length) or MSD-style from the first character (better for strings, avoids needing full-length padding).

### Advanced Questions & Answers

**Q3. Compare LSD vs MSD Radix Sort — why does LSD need every pass to be stable but MSD doesn't strictly?**
A. LSD processes least-significant digit first — correctness relies on each pass preserving the relative order established by *previous* (more significant... wait, less significant) passes, so instability at any digit would corrupt the final order established by digits already processed. MSD processes most-significant digit first and recursively sorts each bucket independently — since buckets are processed in isolation and never merged with cross-bucket ordering concerns, MSD doesn't require strict stability within the recursive sub-sorts (though it needs correct bucket separation).

**Q4. When is Radix Sort a poor choice?**
A. (1) Floating-point numbers — converting them to a radix-sortable representation is non-trivial (though possible via bit-level tricks). (2) Very large or unbounded key ranges without a fixed digit count. (3) Small n where the constant overhead of multiple passes exceeds the benefit — a good comparison sort might win for small inputs. (4) When comparator-based custom ordering (not raw numeric/lexicographic) is needed.

**Q5. How is Radix Sort used in distributed systems, e.g., sorting by IP address?**
A. IPv4 addresses are 32-bit integers — Radix Sort can sort them byte-by-byte (4 passes of Counting Sort over 256 possible byte values), achieving O(n) time versus O(n log n) for comparison sorts. This pattern generalizes to sorting fixed-width keys (IP addresses, fixed-length hashes, timestamps) in large-scale log processing and network analysis pipelines.

---

## 9. Bucket Sort

**Definition:** Distributes elements into a number of "buckets" based on value ranges, sorts each bucket individually (usually with Insertion Sort), then concatenates the buckets in order.

**When to use it:** Sorting **uniformly distributed floating-point or real-valued data** — e.g., normalized scores/probabilities in [0,1). Performs poorly if data is skewed and clusters into few buckets.

### Iterative
```python
def bucket_sort(arr, bucket_count=10):
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / bucket_count or 1
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        idx = min(int((num - min_val) / bucket_range), bucket_count - 1)
        buckets[idx].append(num)
    result = []
    for bucket in buckets:
        result.extend(insertion_sort(bucket))
    return result
```

**Time:** O(n+k) avg, O(n²) worst | **Space:** O(n+k) | **Stable:** Yes | **In-place:** No

### Basic Questions & Answers

**Q1. Why does Bucket Sort assume a uniform distribution of input?**
A. Performance depends on elements being spread roughly evenly across buckets so each bucket has O(1) or O(n/k) elements, making per-bucket sorting cheap. If the distribution is skewed (e.g., all values identical or clustered), most elements land in one bucket, and sorting that bucket with Insertion Sort degrades to O(n²) — the worst case.

**Q2. How does Bucket Sort differ from Counting Sort?**
A. Counting Sort creates one "bucket" (count slot) per *distinct discrete value* and requires integer keys within a bounded range. Bucket Sort creates buckets for *ranges* of values (works for floats/reals too) and sorts within each bucket using another algorithm (commonly Insertion Sort) — it's a generalization suited to continuous data.

### Advanced Questions & Answers

**Q3. Where is Bucket Sort used in real systems?**
A. Sorting uniformly distributed floating-point scores/probabilities (e.g., normalized ML model outputs in [0,1)), histogram-based bucketing/binning in data visualization and analytics pipelines, and as a preprocessing step in radix-like sorts for floating point numbers.

**Q4. What sorting algorithm should you use inside each bucket, and why does it matter?**
A. Insertion Sort is the typical choice because buckets are expected to be small (given uniform distribution assumption), and Insertion Sort has low overhead and good performance on small/nearly-sorted inputs. Using something like Merge Sort inside buckets would add unnecessary constant-factor overhead for small bucket sizes. If buckets can be large or distribution is unknown, a more robust choice (e.g., Quick Sort or even recursively applying Bucket Sort) may be safer.

---

## 10. Shell Sort

**Definition:** A generalization of Insertion Sort that first compares and sorts elements far apart (using a "gap" sequence), then progressively reduces the gap down to 1, at which point it becomes a final, much-cheaper standard Insertion Sort pass.

**When to use it:** Medium-sized arrays, memory-constrained embedded systems needing O(1) space with no recursion, or contexts where a simple, non-recursive algorithm that beats O(n²) in practice is wanted without the complexity of Quick/Merge Sort.

### Iterative
```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
```

**Time:** O(n log n) to O(n²) depending on gaps | **Space:** O(1) | **Stable:** No | **In-place:** Yes

### Basic Questions & Answers

**Q1. Why is Shell Sort a generalization of Insertion Sort?**
A. Shell Sort performs Insertion Sort on elements separated by a "gap" instead of adjacent elements, progressively shrinking the gap to 1 (at which point it's exactly standard Insertion Sort). Early passes with large gaps move elements long distances quickly, so by the time gap=1, the array is nearly sorted and the final Insertion Sort pass is very fast.

**Q2. Why is Shell Sort not stable, even though Insertion Sort is?**
A. Because it compares and swaps elements that are far apart (gap > 1), equal elements can be moved past each other across different gap passes, unlike standard adjacent-only Insertion Sort which never crosses equal elements.

### Advanced Questions & Answers

**Q3. How does the gap sequence affect time complexity?**
A. Shell's original sequence (n/2, n/4, ..., 1) gives worst-case O(n²). Hibbard's sequence (2^k - 1) improves worst case to O(n^1.5). Knuth's sequence (3k+1) gives similar O(n^1.5) bounds. Sedgewick's sequence achieves O(n^4/3). No known gap sequence achieves O(n log n) worst case, but well-chosen sequences get remarkably close in practice — the choice of gap sequence is an active area of empirical (not just theoretical) optimization.

**Q4. When would Shell Sort be preferable over Quick Sort?**
A. (1) Medium-sized arrays where Quick Sort's recursion overhead isn't justified. (2) Memory-constrained embedded systems needing O(1) space with no recursion stack risk. (3) When code simplicity/no-recursion is valued (e.g., simple firmware) while still beating O(n²) algorithms in practice. It's rarely used in large-scale production code today since Quick/Merge/Tim-sort dominate, but it's a good "middle ground" algorithm to discuss for embedded contexts.

---

## Complexity Cheat Sheet

| Algorithm       | Best        | Average     | Worst       | Space     | Stable | In-place |
|-----------------|-------------|-------------|-------------|-----------|--------|----------|
| Bubble Sort     | O(n)        | O(n²)       | O(n²)       | O(1)      | Yes    | Yes      |
| Selection Sort  | O(n²)       | O(n²)       | O(n²)       | O(1)      | No     | Yes      |
| Insertion Sort  | O(n)        | O(n²)       | O(n²)       | O(1)      | Yes    | Yes      |
| Merge Sort      | O(n log n)  | O(n log n)  | O(n log n)  | O(n)      | Yes    | No       |
| Quick Sort      | O(n log n)  | O(n log n)  | O(n²)       | O(log n)  | No     | Yes      |
| Heap Sort       | O(n log n)  | O(n log n)  | O(n log n)  | O(1)      | No     | Yes      |
| Counting Sort   | O(n+k)      | O(n+k)      | O(n+k)      | O(n+k)    | Yes    | No       |
| Radix Sort      | O(d(n+k))   | O(d(n+k))   | O(d(n+k))   | O(n+k)    | Yes    | No       |
| Bucket Sort     | O(n+k)      | O(n+k)      | O(n²)       | O(n+k)    | Yes    | No       |
| Shell Sort      | O(n log n)  | O(n^1.25)*  | O(n²)       | O(1)      | No     | Yes      |

*Depends on gap sequence.

---

## When to Use Which Sort

A quick decision guide — this is exactly the kind of trade-off reasoning Google interviewers probe for.

| Situation | Best Choice | Why |
|---|---|---|
| General-purpose, no special constraints | **Quick Sort** | Fastest in practice on average, in-place, good cache locality |
| Need guaranteed worst-case O(n log n) | **Merge Sort** or **Heap Sort** | No data-dependent degradation to O(n²) |
| Need stability (multi-key sort) | **Merge Sort** (or Insertion/Counting/Radix/Bucket) | Preserves relative order of equal keys |
| Sorting a linked list | **Merge Sort** | Sequential access only, O(1) extra space when merging lists |
| Very limited memory (embedded/real-time) | **Heap Sort** or **Shell Sort** | O(1) extra space, no large recursion stack |
| Small array (<~20 elements) or nearly sorted | **Insertion Sort** | Low overhead, near O(n) on nearly-sorted data |
| Data too large to fit in memory | **External Merge Sort (k-way merge)** | Only needs O(k) elements in memory at once |
| Integers in a small known range (e.g., ages, scores) | **Counting Sort** | O(n+k), beats comparison-sort lower bound |
| Fixed-width integers/strings (e.g., IPs, IDs) | **Radix Sort** | O(d(n+k)), digit-by-digit, no comparisons |
| Uniformly distributed floats (e.g., probabilities) | **Bucket Sort** | Near O(n) when distribution is even |
| Need top-K elements only, not a full sort | **Heap Sort (min/max-heap of size K)** | O(n log k), avoids sorting everything |
| Data has many duplicate keys | **3-way Quick Sort** | Avoids re-sorting the "equal" partition repeatedly |
| Need to find the kth smallest/largest only | **Quickselect** | O(n) average, no need to fully sort |
| Writes are expensive (flash memory/SSD) | **Selection Sort** | Minimum number of swaps (O(n)) |
| Production-grade, real-world mixed data (Python's default) | **Timsort** (`sorted()`/`.sort()`) | Hybrid of Merge + Insertion Sort, exploits existing order in real data |

---

## General Questions — Basic & Advanced (with Answers)

### Basic

**Q1. What is the theoretical lower bound for comparison-based sorting?**
A. Ω(n log n). A comparison sort's execution can be modeled as a binary decision tree where each leaf is a distinct permutation of the input — there are n! possible permutations, so the tree needs at least log₂(n!) leaves. By Stirling's approximation, log₂(n!) ≈ n log₂ n − n log₂ e = Θ(n log n), so any comparison sort needs at least Θ(n log n) comparisons in the worst case.

**Q2. What does "stable sort" mean, and why does it matter?**
A. A stable sort preserves the relative order of elements that compare as equal. It matters when sorting by multiple keys in stages: e.g., to sort employees by department then by salary, you can first sort by salary, then stably sort by department — employees within the same department remain sorted by salary because the second sort didn't disturb their relative order.

**Q3. Difference between in-place and out-of-place sorting?**
A. In-place sorting uses O(1) (or O(log n) for recursion stack) extra memory beyond the input array — e.g., Quick Sort, Heap Sort. Out-of-place sorting requires additional memory proportional to input size — e.g., Merge Sort's O(n) auxiliary arrays. This matters for memory-constrained environments and for sorting datasets close to available RAM limits.

### Advanced

**Q4. How do non-comparison sorts beat the O(n log n) lower bound? What assumption enables this?**
A. They don't violate the lower bound — that bound applies *only* to algorithms that determine order purely through pairwise comparisons. Counting/Radix/Bucket Sort exploit extra structural knowledge about the keys (bounded integer range, fixed digit-width, uniform distribution) to place elements directly using arithmetic (indexing/counting) rather than comparisons, which sidesteps the decision-tree argument entirely.

**Q5. How would you sort data that doesn't fit in memory (external sorting)? Describe k-way merge.**
A. Split the dataset into chunks that fit in RAM, sort each chunk in-memory (any O(n log n) sort) and write each sorted chunk to disk as a "run." Then perform a k-way merge: open a read buffer for each of the k sorted runs, use a min-heap holding the current front element of each run, repeatedly extract the minimum, write it to the output, and refill from the corresponding run. This needs only O(k) elements in memory at once (plus small buffers) regardless of total data size. If there are more runs than can be merged at once, merge in multiple passes (merge k runs at a time until one run remains).

**Q6. Design an API `sort(list, key=None, reverse=False, stable=True)` — how would you implement `key` efficiently?**
A. The standard technique (Schwartzian Transform / decorate-sort-undecorate): map each element to a tuple `(key(element), original_index, element)`, sort these tuples using the natural comparison order of the key (falling back to original_index to guarantee determinism/stability without recomputing `key()` on every comparison), then extract just the elements back out. This ensures `key()` is called exactly n times rather than O(n log n) times during comparisons — a major performance win when `key()` is expensive.
```python
def custom_sort(lst, key=None, reverse=False):
    if key is None:
        key = lambda x: x
    decorated = [(key(item), i, item) for i, item in enumerate(lst)]
    decorated.sort(reverse=reverse)   # ties broken by original index -> stable
    return [item for _, _, item in decorated]
```

**Q7. How would you sort a massive log file by timestamp using limited memory?**
A. External Merge Sort as described in Q5: read the file in memory-sized chunks, sort each chunk by timestamp, write sorted chunks to temp files, then k-way merge the temp files using a min-heap keyed by timestamp, streaming output to the final sorted file without ever loading the whole dataset into memory.

**Q8. How would you sort tasks with dependencies (some depend on others)? Why isn't this a comparison sort?**
A. This is **topological sort**, not a comparison-based total-order sort — dependencies define a partial order (a DAG), not a total order where any two elements are comparable. Use Kahn's algorithm (BFS with in-degree tracking) or DFS-based topological sort. Comparison sorts assume any two elements can be compared and produce a consistent total order; task dependencies may have no defined relationship between unrelated tasks, and cycles (if present) make sorting impossible altogether — a key distinction to flag if an interviewer nudges toward this problem.
```python
from collections import deque, defaultdict

def topological_sort(num_tasks, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * num_tasks
    for src, dst in dependencies:          # src must happen before dst
        graph[src].append(dst)
        in_degree[dst] += 1
    queue = deque([i for i in range(num_tasks) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != num_tasks:
        raise ValueError("Cycle detected — no valid ordering exists")
    return order
```

---

## Coding Problems with Full Solutions

### Basic Tier

**1. Merge Intervals**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
# Time: O(n log n), Space: O(n)
```

**2. Sort Colors (Dutch National Flag)**
```python
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
# Time: O(n), Space: O(1), single pass
```

**3. Kth Largest Element in an Array**
```python
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
# Time: O(n log k), Space: O(k)

# Quickselect alternative — O(n) average:
import random
def kth_largest_quickselect(nums, k):
    target = len(nums) - k          # convert to kth smallest index
    def select(arr, k):
        pivot = random.choice(arr)
        lows = [x for x in arr if x < pivot]
        highs = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]
        if k < len(lows):
            return select(lows, k)
        elif k < len(lows) + len(pivots):
            return pivot
        return select(highs, k - len(lows) - len(pivots))
    return select(nums, target)
```

**4. Relative Sort Array**
```python
def relative_sort_array(arr1, arr2):
    rank = {num: i for i, num in enumerate(arr2)}
    return sorted(arr1, key=lambda x: (rank.get(x, len(arr2)), x))
# Time: O(n log n), Space: O(n)
```

**5. Custom Sort String**
```python
def custom_sort_string(order, s):
    rank = {ch: i for i, ch in enumerate(order)}
    return ''.join(sorted(s, key=lambda c: rank.get(c, len(order))))
# Time: O(n log n), Space: O(n)
```

**6. H-Index**
```python
def h_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h
# Time: O(n log n), Space: O(1) extra (excluding sort)
```

### Advanced Tier

**7. Merge K Sorted Lists**
```python
import heapq

def merge_k_lists(lists):
    """lists: list of Python lists, each already sorted."""
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))   # (value, list_idx, elem_idx)

    result = []
    while heap:
        val, i, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][elem_idx + 1], i, elem_idx + 1))
    return result
# Time: O(N log k) where N = total elements, k = number of lists
# Space: O(k) heap + O(N) output
```

**8. Top K Frequent Elements (Bucket Sort approach — O(n))**
```python
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result
# Time: O(n), Space: O(n)
```

**9. Find Median from Data Stream**
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []   # max-heap (negated values) — lower half
        self.large = []   # min-heap — upper half

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
# Time: O(log n) per insertion, O(1) per median query
# Space: O(n)
```

**10. Largest Number (custom comparator)**
```python
from functools import cmp_to_key

def largest_number(nums):
    strs = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0

    strs.sort(key=cmp_to_key(compare))
    result = ''.join(strs).lstrip('0')
    return result if result else '0'
# Time: O(n log n · m) where m = avg string length, Space: O(n)
```

**11. Count of Smaller Numbers After Self (modified Merge Sort)**
```python
def count_smaller(nums):
    n = len(nums)
    result = [0] * n
    indices = list(range(n))

    def merge_sort(lo, hi):
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        merge_sort(lo, mid)
        merge_sort(mid, hi)
        merged = []
        i, j = lo, mid
        while i < mid and j < hi:
            if nums[indices[i]] <= nums[indices[j]]:
                result[indices[i]] += j - mid   # count elements already placed from right
                merged.append(indices[i]); i += 1
            else:
                merged.append(indices[j]); j += 1
        while i < mid:
            result[indices[i]] += j - mid
            merged.append(indices[i]); i += 1
        while j < hi:
            merged.append(indices[j]); j += 1
        indices[lo:hi] = merged

    merge_sort(0, n)
    return result
# Time: O(n log n), Space: O(n)
```

**12. Kth Smallest Element in a Sorted Matrix (binary search on value range)**
```python
def kth_smallest_matrix(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n - 1][n - 1]

    def count_less_equal(mid):
        count, row, col = 0, n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    while lo < hi:
        mid = (lo + hi) // 2
        if count_less_equal(mid) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo
# Time: O(n log(max-min)), Space: O(1)
```

**13. Employee Free Time**
```python
def employee_free_time(schedule):
    intervals = sorted([iv for emp in schedule for iv in emp], key=lambda x: x[0])
    free_time = []
    end = intervals[0][1]
    for start, e in intervals[1:]:
        if start > end:
            free_time.append([end, start])
        end = max(end, e)
    return free_time
# Time: O(n log n), Space: O(n)
```

**14. Maximum Gap (Bucket Sort in O(n), avoiding a full comparison sort)**
```python
def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    lo, hi = min(nums), max(nums)
    if lo == hi:
        return 0
    n = len(nums)
    bucket_size = max(1, (hi - lo) // (n - 1))
    bucket_count = (hi - lo) // bucket_size + 1
    buckets_min = [None] * bucket_count
    buckets_max = [None] * bucket_count

    for num in nums:
        idx = (num - lo) // bucket_size
        if buckets_min[idx] is None or num < buckets_min[idx]:
            buckets_min[idx] = num
        if buckets_max[idx] is None or num > buckets_max[idx]:
            buckets_max[idx] = num

    max_gap = 0
    prev_max = lo
    for i in range(bucket_count):
        if buckets_min[i] is None:
            continue
        max_gap = max(max_gap, buckets_min[i] - prev_max)
        prev_max = buckets_max[i]
    return max_gap
# Time: O(n), Space: O(n) — uses pigeonhole principle: max gap >= (hi-lo)/(n-1),
# guaranteeing the answer is never *within* one bucket, only *between* buckets.
```

**15. Wiggle Sort**
```python
def wiggle_sort(nums):
    nums.sort()
    n = len(nums)
    mid = (n + 1) // 2
    smaller = nums[:mid][::-1]
    larger = nums[mid:][::-1]
    nums[::2] = smaller
    nums[1::2] = larger
    return nums
# Time: O(n log n), Space: O(n)
```

**16. Sort a Nearly Sorted (K-Sorted) Array**
```python
import heapq

def sort_k_sorted(arr, k):
    heap = arr[:k + 1]
    heapq.heapify(heap)
    result = []
    for i in range(k + 1, len(arr)):
        result.append(heapq.heappushpop(heap, arr[i]))
    while heap:
        result.append(heapq.heappop(heap))
    return result
# Time: O(n log k), Space: O(k)
```

**17. Meeting Rooms II (minimum meeting rooms required)**
```python
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []   # tracks end times of ongoing meetings
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)
# Time: O(n log n), Space: O(n)
```

**18. Sort an Array of 0s, 1s, and 2s (see Sort Colors above) — bonus generalization: k distinct values**
```python
def sort_k_values(arr, k):
    """Counting-sort style approach when values are 0..k-1."""
    count = [0] * k
    for num in arr:
        count[num] += 1
    idx = 0
    for val in range(k):
        for _ in range(count[val]):
            arr[idx] = val
            idx += 1
    return arr
# Time: O(n + k), Space: O(k)
```

---

## Suggested Preparation Strategy

- **Week 1:** Master iterative + recursive versions of Bubble, Selection, Insertion — be able to answer every Basic question above from memory and derive complexity on a whiteboard.
- **Week 2:** Deep-dive Merge Sort and Quick Sort — write both from memory, and be ready to answer every Advanced question (stability, in-place trade-offs, Quickselect, 3-way partitioning, external sorting).
- **Week 3:** Heap Sort + priority-queue-based problems (Merge K Lists, Kth Largest, Top K Frequent, Median from Data Stream).
- **Week 4:** Non-comparison sorts (Counting, Radix, Bucket) — know exactly when they apply, their limitations, and practice the "Maximum Gap" / "Top K Frequent" style problems that use them cleverly.
- **Throughout:** For every algorithm, be ready to answer: *"Why this one and not another, given these constraints (memory, stability, data distribution, data size)?"* — Google interviewers weight **trade-off reasoning** far more heavily than memorized code.
