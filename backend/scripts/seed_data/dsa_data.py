"""
DSA Topics and Lessons Seed Data
Incorporating concepts from:
- python_interview/DSA/time_complexity.md
- python_interview/DSA/dsa_question.md
- python_interview/DSA_questions.md
- python_interview/DSA/sorts/bubble_sort.md
- python_interview/DSA/sorts/sorting_algorithms_beginner_guide.md
- python_interview/DSA/sorts/sorting_algorithms_interview_prep_v2.md
"""

DSA_TOPICS = [
    {
        "subjectSlug": "dsa",
        "title": "Asymptotic Analysis & Time-Space Complexity",
        "slug": "time-space-complexity",
        "description": "Understand Big-O asymptotic growth, runtime analysis, and memory trade-offs in Python algorithms.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "dsa",
        "title": "Arrays & Dynamic Lists",
        "slug": "arrays",
        "description": "Explore contiguous memory layout, O(1) indexing arithmetic, CPython dynamic list growth factor, and two-pointer patterns.",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "dsa",
        "title": "Searching Algorithms",
        "slug": "searching-algorithms",
        "description": "Master linear search and divide-and-conquer binary search with search-space halving techniques.",
        "order": 3,
        "isPublished": True,
    },
    {
        "subjectSlug": "dsa",
        "title": "Sorting Algorithms Complete Guide",
        "slug": "sorting-algorithms",
        "description": "Comprehensive guide to Bubble, Selection, Insertion, Merge, Quick Sort, and Python's Timsort with stability and space-time breakdowns.",
        "order": 4,
        "isPublished": True,
    },
]

DSA_LESSONS = [
    # -------------------------------------------------------------------------
    # Topic 1: Asymptotic Analysis & Time-Space Complexity
    # -------------------------------------------------------------------------
    {
        "topicSlug": "time-space-complexity",
        "subjectSlug": "dsa",
        "title": "Time Complexity & Big-O Foundations",
        "slug": "time-complexity-foundations",
        "description": "Learn what Big-O notation measures, how to evaluate runtime independently of hardware, and master common complexity classes.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is Time Complexity?",
                    "content": (
                        "Time complexity measures how the execution time of an algorithm grows as the size of the input (n) increases. "
                        "It does NOT measure time in seconds, because clock seconds depend on your machine's processor, memory, and background processes. "
                        "Instead, Big-O measures the number of basic operations relative to input size n.\n\n"
                        "Why is this vital for software engineers? An algorithm that runs instantly on 10 items might freeze your entire application when running on 1,000,000 items!"
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Rule of Thumb: Big-O represents the upper bound (worst-case scenario), Omega (Ω) represents the lower bound (best-case), and Theta (Θ) represents the tight bound (average case)."
                },
                {
                    "type": "explanation",
                    "title": "The Hierarchy of Common Time Complexities",
                    "content": (
                        "1. O(1) - Constant Time: Runs in fixed steps regardless of n. Example: Accessing array element by index or dict lookup.\n"
                        "2. O(log n) - Logarithmic Time: The problem size is halved at every step. Extremely fast! Example: Binary search.\n"
                        "3. O(n) - Linear Time: Operations scale directly with input size. Example: A single loop iterating over a list.\n"
                        "4. O(n log n) - Linearithmic Time: Splitting into halves and scanning. Example: Merge Sort, Timsort, Quick Sort.\n"
                        "5. O(n²) - Quadratic Time: Nested loops comparing elements. Feasible for small n (~1,000), but chokes on large data. Example: Bubble Sort.\n"
                        "6. O(2ⁿ) - Exponential Time: Doubles with each added element. Example: Recursive Fibonacci without memoization.\n"
                        "7. O(n!) - Factorial Time: All permutations. Highly inefficient for n > 12. Example: Brute-force Traveling Salesperson."
                    )
                },
                {
                    "type": "code",
                    "title": "Comparing Complexity Classes in Python",
                    "language": "python",
                    "code": (
                        "# O(1) - Constant Time: 1 operation regardless of list size\n"
                        "def get_first_element(arr):\n"
                        "    return arr[0] if arr else None\n\n"
                        "# O(n) - Linear Time: n operations\n"
                        "def find_max(arr):\n"
                        "    max_val = arr[0]\n"
                        "    for num in arr:          # runs n times\n"
                        "        if num > max_val:\n"
                        "            max_val = num\n"
                        "    return max_val\n\n"
                        "# O(n^2) - Quadratic Time: n * n operations\n"
                        "def print_all_pairs(arr):\n"
                        "    for i in arr:            # runs n times\n"
                        "        for j in arr:        # runs n times for each i\n"
                        "            print(i, j)"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Pro-Tip: In coding interviews, drop constants and lower-order terms. 3n² + 5n + 100 simplifies directly to O(n²)."
                }
            ]
        }
    },
    {
        "topicSlug": "time-space-complexity",
        "subjectSlug": "dsa",
        "title": "Space Complexity & Memory Bounds",
        "slug": "space-complexity-memory",
        "description": "Understand auxiliary space vs input space, stack memory usage during recursion, and techniques to minimize memory footprint.",
        "estimatedTime": "20 mins",
        "difficulty": "Beginner",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Auxiliary Space vs Input Space",
                    "content": (
                        "Space complexity is the total memory space required by an algorithm to execute as a function of the input size n.\n\n"
                        "• Input Space: The memory required to hold the inputs themselves (e.g., an incoming array of 1,000,000 integers).\n"
                        "• Auxiliary Space: The extra or temporary memory allocated by the algorithm to solve the problem (e.g., helper arrays, hash maps, variables).\n\n"
                        "When interviewers ask 'What is the space complexity?', they almost always mean Auxiliary Space."
                    )
                },
                {
                    "type": "code",
                    "title": "O(1) Auxiliary Space vs O(n) Auxiliary Space",
                    "language": "python",
                    "code": (
                        "# O(1) Auxiliary Space: In-place reversal using two pointers\n"
                        "def reverse_in_place(arr):\n"
                        "    left, right = 0, len(arr) - 1\n"
                        "    while left < right:\n"
                        "        arr[left], arr[right] = arr[right], arr[left]\n"
                        "        left += 1\n"
                        "        right -= 1\n"
                        "    return arr  # Modified original array, no new list created\n\n"
                        "# O(n) Auxiliary Space: Creating a brand new list\n"
                        "def reverse_with_new_list(arr):\n"
                        "    new_arr = []\n"
                        "    for item in reversed(arr):\n"
                        "        new_arr.append(item)  # Allocates n new memory slots\n"
                        "    return new_arr"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Recursion Call Stack & Memory Frames",
                    "content": (
                        "Every recursive call creates a new stack frame in memory storing local variables and return addresses. "
                        "If a recursive function recurses n times before hitting a base case, it consumes O(n) stack memory even if no variables are created!\n\n"
                        "Example: Naive factorial of n calls factorial(n-1) all the way down to 1, building a stack of depth n -> O(n) space complexity."
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Recursion Depth Limit: Python sets a default recursion limit of 1000 frames (`sys.getrecursionlimit()`). Exceeding this triggers RecursionError: maximum recursion depth exceeded."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 2: Arrays & Dynamic Lists
    # -------------------------------------------------------------------------
    {
        "topicSlug": "arrays",
        "subjectSlug": "dsa",
        "title": "What is an Array? Contiguous Memory & Architecture",
        "slug": "what-is-an-array",
        "description": "Discover why arrays live in contiguous RAM blocks, why index lookup is an instant O(1) formula, and why insertion is O(n).",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": "ArrayVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is an Array in Memory?",
                    "content": (
                        "An array is a linear data structure that stores elements in consecutive, contiguous memory locations in RAM. "
                        "Because every element has a uniform byte size and elements sit side-by-side, the computer does NOT need to scan through elements to find index i."
                    )
                },
                {
                    "type": "visualization",
                    "component": "ArrayVisualizer",
                    "initialState": {"items": [12, 28, 45, 67, 89, 102]}
                },
                {
                    "type": "explanation",
                    "title": "The Math Formula Behind O(1) Index Access",
                    "content": (
                        "When you request `arr[i]`, the CPU calculates the exact RAM memory address in a single instruction:\n\n"
                        "Address(arr[i]) = Base_Address + (i * Element_Size_In_Bytes)\n\n"
                        "Example: If an integer array starts at memory address 1000 and each integer takes 4 bytes:\n"
                        "• arr[0] = 1000 + (0 * 4) = 1000\n"
                        "• arr[3] = 1000 + (3 * 4) = 1012\n\n"
                        "Because this is a simple multiplication and addition, it executes in exactly 1 clock cycle -> O(1) Constant Time!"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Why Insertion and Deletion are O(n)",
                    "content": (
                        "To insert a new element at index 0 or in the middle of an array, every subsequent element must be physically shifted one slot to the right in RAM to make room. "
                        "In the worst case (inserting at the beginning), all n elements must shift -> O(n) Linear Time."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "In Python, a standard list is NOT a linked list. It is an array of memory pointers pointing to PyObject instances in the heap."
                }
            ]
        }
    },
    {
        "topicSlug": "arrays",
        "subjectSlug": "dsa",
        "title": "Dynamic Arrays & Python List Internals",
        "slug": "dynamic-arrays-python-lists",
        "description": "Understand how CPython dynamically over-allocates list capacity and achieves amortized O(1) append operations.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Static Array vs Dynamic Array",
                    "content": (
                        "• Static Array (C/Java): Fixed size allocated at initialization. Cannot grow or shrink.\n"
                        "• Dynamic Array (Python `list`, Java `ArrayList`): Automatically grows when full by allocating a larger array in a new memory location and copying existing items."
                    )
                },
                {
                    "type": "explanation",
                    "title": "How Python Over-Allocates Memory (CPython Growth Factor)",
                    "content": (
                        "If Python resized its list on every single append, appending n items would take O(n²) time! "
                        "Instead, CPython uses geometric over-allocation with the internal growth formula:\n\n"
                        "`new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6) + newsize`\n\n"
                        "This produces allocated capacities of: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88... slots!\n"
                        "Because resizes happen exponentially less often as the list grows, the cost of copying elements spreads out over all appends."
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Amortized O(1) Meaning: 99% of appends take O(1) time (writing to pre-allocated empty slots). Only 1% trigger an O(n) copy. Averaged over n operations, each append costs O(1)."
                },
                {
                    "type": "code",
                    "title": "Inspecting List Allocation in Python",
                    "language": "python",
                    "code": (
                        "import sys\n\n"
                        "data = []\n"
                        "prev_bytes = sys.getsizeof(data)\n"
                        "print(f'Length: 0, Size: {prev_bytes} bytes')\n\n"
                        "for i in range(25):\n"
                        "    data.append(i)\n"
                        "    curr_bytes = sys.getsizeof(data)\n"
                        "    if curr_bytes != prev_bytes:\n"
                        "        print(f'Length: {len(data)}, Resized to: {curr_bytes} bytes!')\n"
                        "        prev_bytes = curr_bytes"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "arrays",
        "subjectSlug": "dsa",
        "title": "Two Pointers & Sliding Window Patterns",
        "slug": "two-pointers-sliding-window",
        "description": "Master the two most tested array patterns: Two Pointers and Sliding Window with practical interview solutions.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": "ArrayVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Two Pointers Technique",
                    "content": (
                        "The Two Pointers pattern uses two integer index variables (e.g., `left` and `right`) that traverse an array "
                        "either towards each other from opposite ends, or in tandem in the same direction. "
                        "It eliminates nested loops and transforms naive O(n²) algorithms into optimal O(n) linear solutions."
                    )
                },
                {
                    "type": "code",
                    "title": "Two Sum: Naive O(n²) Brute Force vs Optimal O(n) Hash Map",
                    "language": "python",
                    "code": (
                        "# Brute Force: Check every pair -> O(n^2) Time, O(1) Space\n"
                        "def two_sum_brute(nums, target):\n"
                        "    for i in range(len(nums)):\n"
                        "        for j in range(i + 1, len(nums)):\n"
                        "            if nums[i] + nums[j] == target:\n"
                        "                return [i, j]\n"
                        "    return []\n\n"
                        "# Optimal: Store complements in Hash Map -> O(n) Time, O(n) Space\n"
                        "def two_sum_optimal(nums, target):\n"
                        "    seen = {}  # complement -> index\n"
                        "    for i, num in enumerate(nums):\n"
                        "        complement = target - num\n"
                        "        if complement in seen:\n"
                        "            return [seen[complement], i]\n"
                        "        seen[num] = i\n"
                        "    return []"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Maximum Subarray: Kadane's Algorithm",
                    "content": (
                        "Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.\n\n"
                        "Kadane's Insight: As we iterate through the array, at each position we decide whether to add the current number "
                        "to our existing running sum, or reset and start a fresh subarray from the current number: `max(num, current_sum + num)`."
                    )
                },
                {
                    "type": "code",
                    "title": "Kadane's Algorithm in Python",
                    "language": "python",
                    "code": (
                        "def max_subarray(nums):\n"
                        "    current_sum = nums[0]\n"
                        "    max_sum = nums[0]\n\n"
                        "    for num in nums[1:]:\n"
                        "        # Either continue the running subarray or start fresh\n"
                        "        current_sum = max(num, current_sum + num)\n"
                        "        max_sum = max(max_sum, current_sum)\n\n"
                        "    return max_sum\n\n"
                        "# Example:\n"
                        "# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\n"
                        "# Output: 6 (from subarray [4, -1, 2, 1])"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Complexity: Kadane's algorithm executes in O(n) time and uses O(1) auxiliary space, down from the O(n³) naive brute force approach!"
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 3: Searching Algorithms
    # -------------------------------------------------------------------------
    {
        "topicSlug": "searching-algorithms",
        "subjectSlug": "dsa",
        "title": "Linear Search vs Binary Search Mastery",
        "slug": "binary-search-mastery",
        "description": "Understand how Binary Search repeatedly halves search spaces in sorted data, reducing 1 billion items to just 30 comparisons.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": "BinarySearchVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Power of Halving: O(log n)",
                    "content": (
                        "Linear search checks each element one by one from index 0 to n-1. In the worst case, it takes n operations.\n\n"
                        "Binary Search requires a SORTED array. At each step, it compares the target to the middle element:\n"
                        "• If target == mid: found!\n"
                        "• If target < mid: target must lie in the left half, so discard the right half (`right = mid - 1`).\n"
                        "• If target > mid: target must lie in the right half, so discard the left half (`left = mid + 1`).\n\n"
                        "Because the remaining search space halves on every single iteration, searching across 1,000,000 elements takes at most 20 comparisons (log₂ 1,000,000 ≈ 20)!"
                    )
                },
                {
                    "type": "visualization",
                    "component": "BinarySearchVisualizer",
                    "initialState": {"items": [4, 9, 15, 23, 38, 45, 56, 72, 88, 99]}
                },
                {
                    "type": "code",
                    "title": "Binary Search Implementation in Python",
                    "language": "python",
                    "code": (
                        "def binary_search(arr, target):\n"
                        "    left = 0\n"
                        "    right = len(arr) - 1\n\n"
                        "    while left <= right:\n"
                        "        # Safe middle calculation avoiding integer overflow in typed languages\n"
                        "        mid = left + (right - left) // 2\n\n"
                        "        if arr[mid] == target:\n"
                        "            return mid  # Found at index mid\n"
                        "        elif arr[mid] < target:\n"
                        "            left = mid + 1   # Search right half\n"
                        "        else:\n"
                        "            right = mid - 1  # Search left half\n\n"
                        "    return -1  # Target does not exist"
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Critical Precondition: Binary Search ONLY works on sorted arrays. If the input is unsorted, sorting it first takes O(n log n), which is only worthwhile if multiple searches will be performed."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 4: Sorting Algorithms Complete Guide
    # -------------------------------------------------------------------------
    {
        "topicSlug": "sorting-algorithms",
        "subjectSlug": "dsa",
        "title": "Bubble Sort & Early-Exit Optimization",
        "slug": "bubble-sort-deep-dive",
        "description": "Understand bubble sort mechanics, pass-by-pass dry runs, the swapped optimization flag, and stability characteristics.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": "SortingVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "How Bubble Sort Works",
                    "content": (
                        "Bubble Sort is a comparison-based sorting algorithm. It works by repeatedly comparing adjacent elements "
                        "and swapping them if they are in the wrong order. "
                        "With each complete pass through the array, the largest unsorted element 'bubbles up' to its correct final position at the end of the array."
                    )
                },
                {
                    "type": "visualization",
                    "component": "SortingVisualizer",
                    "initialState": {"items": [64, 34, 25, 12, 22, 11, 90]}
                },
                {
                    "type": "code",
                    "title": "Optimized Bubble Sort Implementation",
                    "language": "python",
                    "code": (
                        "def bubble_sort(arr):\n"
                        "    n = len(arr)\n"
                        "    for i in range(n):\n"
                        "        # Optimization flag: detect if any swaps occurred in this pass\n"
                        "        swapped = False\n\n"
                        "        # Last i elements are already in place\n"
                        "        for j in range(0, n - i - 1):\n"
                        "            if arr[j] > arr[j + 1]:\n"
                        "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n"
                        "                swapped = True\n\n"
                        "        # If no two elements were swapped, array is ALREADY sorted!\n"
                        "        if not swapped:\n"
                        "            break\n\n"
                        "    return arr"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Complexity & Properties Breakdown",
                    "content": (
                        "• Worst-Case Time: O(n²) when array is reversed.\n"
                        "• Average-Case Time: O(n²).\n"
                        "• Best-Case Time: O(n) with the `swapped` flag when the array is already sorted!\n"
                        "• Auxiliary Space: O(1) In-place (only swapping elements).\n"
                        "• Stability: Stable (equal elements retain their relative order because we only swap when `arr[j] > arr[j+1]`, strictly greater)."
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Insight: Without the `swapped` boolean check, Bubble Sort would needlessly execute all n² operations even on an already-sorted array!"
                }
            ]
        }
    },
    {
        "topicSlug": "sorting-algorithms",
        "subjectSlug": "dsa",
        "title": "Selection Sort & Insertion Sort",
        "slug": "selection-insertion-sort",
        "description": "Examine Selection Sort (finding minimums) and Insertion Sort (card-player shifting) with stability comparisons.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": "SortingVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Selection Sort: Finding the Minimum",
                    "content": (
                        "Selection Sort divides the array into a sorted sublist at the left and an unsorted sublist at the right. "
                        "In each pass, it finds the smallest element in the unsorted sublist and swaps it with the first unsorted element.\n\n"
                        "Key Fact: Selection Sort ALWAYS takes O(n²) time, even if the array is already sorted, because it must scan the entire unsorted segment to guarantee it found the true minimum."
                    )
                },
                {
                    "type": "code",
                    "title": "Selection Sort in Python",
                    "language": "python",
                    "code": (
                        "def selection_sort(arr):\n"
                        "    n = len(arr)\n"
                        "    for i in range(n):\n"
                        "        min_idx = i\n"
                        "        for j in range(i + 1, n):\n"
                        "            if arr[j] < arr[min_idx]:\n"
                        "                min_idx = j\n"
                        "        # Swap minimum element into sorted prefix\n"
                        "        arr[i], arr[min_idx] = arr[min_idx], arr[i]\n"
                        "    return arr"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Insertion Sort: The Playing Cards Algorithm",
                    "content": (
                        "Think of how you sort playing cards in your hand: You pick up one card at a time and slide it backwards into its correct position among the already-sorted cards.\n\n"
                        "Why Insertion Sort is brilliant: For small arrays (n < 50) or arrays that are already nearly sorted, Insertion Sort runs in O(n) linear time with minimal overhead! This is why production engines (like Python's Timsort) use Insertion Sort for small slices."
                    )
                },
                {
                    "type": "code",
                    "title": "Insertion Sort in Python",
                    "language": "python",
                    "code": (
                        "def insertion_sort(arr):\n"
                        "    for i in range(1, len(arr)):\n"
                        "        key = arr[i]\n"
                        "        j = i - 1\n"
                        "        # Shift elements greater than key to one position ahead\n"
                        "        while j >= 0 and arr[j] > key:\n"
                        "            arr[j + 1] = arr[j]\n"
                        "            j -= 1\n"
                        "        arr[j + 1] = key\n"
                        "    return arr"
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Stability Difference: Insertion Sort is STABLE. Selection Sort is UNSTABLE because long-distance swapping can leapfrog duplicate values."
                }
            ]
        }
    },
    {
        "topicSlug": "sorting-algorithms",
        "subjectSlug": "dsa",
        "title": "Merge Sort & Divide-and-Conquer",
        "slug": "merge-sort-divide-conquer",
        "description": "Master recursive divide-and-conquer splitting and merging with guaranteed O(n log n) runtime performance.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": "SortingVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Divide-and-Conquer Paradigm",
                    "content": (
                        "Merge Sort breaks the problem into three elegant phases:\n\n"
                        "1. Divide: Recursively split the array down the middle until each sub-array contains only 1 element (a 1-element list is inherently sorted).\n"
                        "2. Conquer: Recursively sort both sub-arrays.\n"
                        "3. Combine (Merge): Merge the two sorted halves into a single sorted list by comparing front elements."
                    )
                },
                {
                    "type": "code",
                    "title": "Merge Sort Implementation in Python",
                    "language": "python",
                    "code": (
                        "def merge_sort(arr):\n"
                        "    if len(arr) <= 1:\n"
                        "        return arr\n\n"
                        "    mid = len(arr) // 2\n"
                        "    left = merge_sort(arr[:mid])\n"
                        "    right = merge_sort(arr[mid:])\n\n"
                        "    return merge(left, right)\n\n"
                        "def merge(left, right):\n"
                        "    result = []\n"
                        "    i = j = 0\n\n"
                        "    while i < len(left) and j < len(right):\n"
                        "        if left[i] <= right[j]:  # <= ensures algorithm remains stable\n"
                        "            result.append(left[i])\n"
                        "            i += 1\n"
                        "        else:\n"
                        "            result.append(right[j])\n"
                        "            j += 1\n\n"
                        "    result.extend(left[i:])\n"
                        "    result.extend(right[j:])\n"
                        "    return result"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Why Time is ALWAYS O(n log n)",
                    "content": (
                        "• Number of levels in the recursion tree: log₂ n (halving at each level).\n"
                        "• Work done per level during merging: O(n) operations across all sub-arrays.\n"
                        "• Total Time = log₂ n levels * n work per level = O(n log n).\n"
                        "Unlike Quick Sort, Merge Sort NEVER degrades to O(n²), making it reliable for predictable SLAs."
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Tradeoff: Merge Sort requires O(n) auxiliary space to hold temporary merged sub-arrays, making it memory-intensive compared to in-place sorts."
                }
            ]
        }
    },
    {
        "topicSlug": "sorting-algorithms",
        "subjectSlug": "dsa",
        "title": "Quick Sort & Partitioning Strategies",
        "slug": "quick-sort-partitioning",
        "description": "Understand pivot selection, Lomuto vs Hoare partitioning schemes, and why Quick Sort is the preferred in-memory sorting engine.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 4,
        "isPublished": True,
        "interactiveType": "SortingVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "How Quick Sort Works",
                    "content": (
                        "Quick Sort selects a 'pivot' element from the array and partitions the remaining elements into two buckets:\n"
                        "• Elements smaller than the pivot go to the left.\n"
                        "• Elements greater than the pivot go to the right.\n\n"
                        "Once partitioned, the pivot is in its final, permanently sorted position. Quick Sort then recurses on the left and right sub-arrays."
                    )
                },
                {
                    "type": "code",
                    "title": "In-Place Quick Sort (Lomuto Partition Scheme)",
                    "language": "python",
                    "code": (
                        "def quick_sort(arr, low, high):\n"
                        "    if low < high:\n"
                        "        pi = partition(arr, low, high)\n"
                        "        quick_sort(arr, low, pi - 1)\n"
                        "        quick_sort(arr, pi + 1, high)\n"
                        "    return arr\n\n"
                        "def partition(arr, low, high):\n"
                        "    pivot = arr[high]  # Choose last element as pivot\n"
                        "    i = low - 1        # Pointer for smaller element\n\n"
                        "    for j in range(low, high):\n"
                        "        if arr[j] <= pivot:\n"
                        "            i += 1\n"
                        "            arr[i], arr[j] = arr[j], arr[i]\n\n"
                        "    # Place pivot in its correct position\n"
                        "    arr[i + 1], arr[high] = arr[high], arr[i + 1]\n"
                        "    return i + 1"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Average Case vs Worst Case",
                    "content": (
                        "• Average Time: O(n log n) with excellent cache locality because swaps occur in-place.\n"
                        "• Worst Case Time: O(n²) when the pivot chosen is consistently the smallest or largest element (e.g., sorting an already-sorted array with last element as pivot).\n"
                        "• Space Complexity: O(log n) auxiliary stack space for recursion frames.\n"
                        "• Mitigation: Use Random Pivot selection or Median-of-Three (first, middle, last) to virtually eliminate the worst case in production."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Stability Note: Quick Sort is UNSTABLE because partitioning swaps items over large distances."
                }
            ]
        }
    },
    {
        "topicSlug": "sorting-algorithms",
        "subjectSlug": "dsa",
        "title": "Sorting Algorithms Comparison & Python Timsort",
        "slug": "sorting-comparison-timsort",
        "description": "Master the definitive interview comparison cheat-sheet and understand Python's internal hybrid algorithm: Timsort.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 5,
        "isPublished": True,
        "interactiveType": "SortingVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Master Sorting Comparison Table",
                    "content": (
                        "| Algorithm | Best Time | Average Time | Worst Time | Space | Stable? | In-Place? |\n"
                        "|---|---|---|---|---|---|---|\n"
                        "| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |\n"
                        "| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |\n"
                        "| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |\n"
                        "| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |\n"
                        "| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |\n"
                        "| Timsort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No |"
                    )
                },
                {
                    "type": "explanation",
                    "title": "What is Python's Timsort?",
                    "content": (
                        "Created by Tim Peters in 2002 for Python (now also used in Java standard library and Android), "
                        "Timsort is a hybrid adaptive sorting algorithm combining Merge Sort and Insertion Sort.\n\n"
                        "How Timsort Operates:\n"
                        "1. Identifies 'runs': Real-world data is rarely purely random; it already contains naturally ascending or descending chunks.\n"
                        "2. For short runs (min-run size ~32-64 items), it uses Insertion Sort, which has negligible overhead.\n"
                        "3. It then merges these balanced runs using an optimized Merge Sort with 'galloping mode' to fast-forward past duplicate segments."
                    )
                },
                {
                    "type": "code",
                    "title": "Python's Built-in Timsort: list.sort() vs sorted()",
                    "language": "python",
                    "code": (
                        "numbers = [42, 12, 88, 3, 27]\n\n"
                        "# 1. In-place sort (mutates original list, returns None)\n"
                        "numbers.sort()\n"
                        "print('In-place:', numbers)  # [3, 12, 27, 42, 88]\n\n"
                        "# 2. sorted() function (creates brand-new sorted list, works on any iterable)\n"
                        "words = ('zebra', 'apple', 'mango')\n"
                        "new_sorted = sorted(words, key=len, reverse=True)\n"
                        "print('By length descending:', new_sorted)  # ['zebra', 'apple', 'mango']"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Golden Rule: In Python interviews, default to using sorted() or list.sort() unless the interviewer explicitly asks you to implement an algorithm from scratch."
                }
            ]
        }
    }
]
