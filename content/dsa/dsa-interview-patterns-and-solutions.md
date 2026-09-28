

# 🚀 PHASE 1: Normal Companies (Foundation + Practical DSA)

👉 Focus: **Basics + Clean logic + Implementation**

## 🔹 1. Arrays & Strings (MOST IMPORTANT)

These are asked in almost every first round.

**Questions:**

1. Two Sum
   → LeetCode: *Two Sum*
    ### questions :
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
        
        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]
        nums =
        input : [3,2,3], target = 6
        Output : [0,2]

    ### 💡 Solution (Brute Force)

             class Solution(object):
                def twoSum(self, nums, target):
                    """
                    :type nums: List[int]
                    :type target: int
                    :rtype: List[int]
                    """
                    for i in range(len(nums)-1):
                        for j in range(i+1,len(nums)):
                            if nums[i] + nums[j] == target:
                                print("yes")
                                return [i,j]
        
        # 🔍 1. Time Complexity of Your Solution (Brute Force)

        ### Your Code:

        ```python
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        ```

        ### ⏱️ Time Complexity: **O(n²)**

        ### Why?

        * Outer loop runs → **n times**
        * Inner loop runs → **(n-1), (n-2), ..., 1**
        * Total operations:

        ```
        n + (n-1) + (n-2) + ... + 1 = n(n-1)/2
        ```

        👉 Which simplifies to **O(n²)**

        ---

        ### 💾 Space Complexity: **O(1)**

        * No extra space used (just variables)

        ---

        ### ⚡ 2. Optimized Solution (HashMap / Dictionary)

            ## 💡 Idea:

            Instead of checking every pair:

            * Store numbers in a **hash map**
            * For each number, check if its complement exists

            ```
            complement = target - current_number
            ```

            ---

            ## ✅ Optimized Code

            ```python
            class Solution(object):
                def twoSum(self, nums, target):
                    hashmap = {}

                    for i in range(len(nums)):
                        complement = target - nums[i]

                        if complement in hashmap:
                            return [hashmap[complement], i]

                        hashmap[nums[i]] = i
            ```

            ---

            # 🚀 Complexity of Optimized Solution

            ### ⏱️ Time Complexity: **O(n)**

            * We traverse the array **once**
            * HashMap lookup → **O(1)**

            👉 Total = **O(n)**

            ---

            ### 💾 Space Complexity: **O(n)**

            * In worst case, we store all elements in hashmap

            ---

            # 🔥 Dry Run (VERY IMPORTANT FOR INTERVIEW)

            ```
            nums = [2,7,11,15], target = 9
            ```

            | Step | num | complement | hashmap | action               |
            | ---- | --- | ---------- | ------- | -------------------- |
            | 0    | 2   | 7          | {}      | store {2:0}          |
            | 1    | 7   | 2          | {2:0}   | FOUND → return [0,1] |

            ---

            # 🎯 Final Comparison

            | Approach    | Time  | Space | Interview Level |
            | ----------- | ----- | ----- | --------------- |
            | Brute Force | O(n²) | O(1)  | ❌ Basic         |
            | HashMap     | O(n)  | O(n)  | ✅ Expected      |

            ---

            # 💡 Interview Tip (VERY IMPORTANT)

            If interviewer asks:
            👉 *“Can you optimize this?”*

            You should say:

            > "Yes, we can reduce time complexity from O(n²) to O(n) using a hash map to store visited elements and check complements in constant time."




2. Best Time to Buy and Sell Stock
   → LeetCode: *Best Time to Buy and Sell Stock*
   ### question
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        

        Example 1:

        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
        Example 2:

        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.

    ### solution
    # 🟥 1. Brute Force Solution

            ## 💻 Code

            ```python
            def maxProfit(prices):
                profit = 0
                n = len(prices)

                for i in range(n - 1):
                    for j in range(i + 1, n):
                        new_profit = prices[j] - prices[i]
                        profit = max(profit, new_profit)

                return profit
            ```

            ---

            ## ⏱ Time Complexity Explanation

            ### 🔁 Loops:

            * Outer loop runs → **n times**
            * Inner loop runs → **(n-1), (n-2), ..., 1**

            👉 Total operations:
            [
            (n-1) + (n-2) + ... + 1 = \frac{n(n-1)}{2}
            ]

            ### ✅ Final Complexity:

            * **Time Complexity:** **O(n²)**
            * **Space Complexity:** **O(1)**

            ---

            ## ❌ Why it's slow?

            Because you're:

            * Checking **every possible buy-sell pair**
            * Even when unnecessary

            ---

    # 🟢 2. Optimized Solution (Best Approach)

            ## 💻 Code

            ```python
            def maxProfit(prices):
                min_price = float('inf')
                profit = 0

                for price in prices:
                    min_price = min(min_price, price)
                    profit = max(profit, price - min_price)

                return profit
            ```

            ---

            ## 💡 Intuition

            Instead of checking all pairs:

            * Keep track of **lowest price so far**
            * At each step, calculate:

            ```
            profit = current_price - min_price
            ```

            ---

            ## ⏱ Time Complexity Explanation

            ### 🔁 Loop:

            * Single loop → runs **n times**

            ### ⚡ Operations inside loop:

            * Constant time → O(1)

            ### ✅ Final Complexity:

            * **Time Complexity:** **O(n)**
            * **Space Complexity:** **O(1)**

            ---

            # ⚖️ Comparison

            | Approach    | Time Complexity | Space | Efficiency |
            | ----------- | --------------- | ----- | ---------- |
            | Brute Force | O(n²) ❌         | O(1)  | Slow       |
            | Optimized   | O(n) ✅          | O(1)  | Fast       |

            ---




3. Move Zeroes
   → LeetCode: *Move Zeroes*
   ### Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
      Note that you must do this in-place without making a copy of the array.
         Example 1:

         Input: nums = [0,1,0,3,12]
         Output: [1,3,12,0,0]
         Example 2:

         Input: nums = [0]
         Output: [0]
         

         Constraints:

         1 <= nums.length <= 104
         -231 <= nums[i] <= 231 - 1

                  
         # 🔴 1. Your Approach (Brute Force)

         ### 💻 Code (Your version)

         ```python
         def moveZeroes(nums):
            nums2 = []
            
            for i in range(len(nums)):
               if nums[i] != 0:
                     nums2.append(nums[i])

            for i in range(len(nums2)):
               nums[i] = nums2[i]

            for i in range(len(nums2), len(nums)):
               nums[i] = 0
         ```

         ---

         ## ⏱ Time Complexity

         Let `n = len(nums)`

         * First loop → O(n)
         * Second loop → O(n)
         * Third loop → O(n)

         👉 Total:

         ```
         O(n) + O(n) + O(n) = O(n)
         ```

         ✅ **Time Complexity = O(n)**

         ---

         ## 📦 Space Complexity

         * You created a new array `nums2`

         👉 In worst case (no zeros):

         ```
         nums2 size = n
         ```

         ❌ **Space Complexity = O(n)**

         ---

         ## ❌ Why This Is Not Optimal

         * Problem says: **"Do it in-place"**
         * You're using extra memory → not allowed in strict interviews

         ---

         # 🟢 2. Optimized Approach (Two Pointer)

         ## 💡 Idea (VERY IMPORTANT)

         * Maintain a pointer `k`
         * Place all non-zero elements at the front
         * Fill remaining positions with 0

         ---

         ## 💻 Optimized Code

         ```python
         def moveZeroes(nums):
            k = 0  # position to place next non-zero

            # Step 1: Move non-zero elements forward
            for i in range(len(nums)):
               if nums[i] != 0:
                     nums[k] = nums[i]
                     k += 1

            # Step 2: Fill remaining with zeros
            for i in range(k, len(nums)):
               nums[i] = 0
         ```

         ---

         ## 🔁 Example Walkthrough

         ```
         nums = [0,1,0,3,12]
         ```

         After Step 1:

         ```
         [1,3,12,_,_]
         ```

         After Step 2:

         ```
         [1,3,12,0,0]
         ```

         ---

         ## ⏱ Time Complexity

         * First loop → O(n)
         * Second loop → O(n)

         👉 Total:

         ```
         O(n)
         ```

         ✅ **Time Complexity = O(n)**

         ---

         ## 📦 Space Complexity

         * No extra array used
         * Only variable `k`

         ✅ **Space Complexity = O(1)**

         ---

         # 🚀 EVEN BETTER (Single Pass Swap Approach)

         👉 This is the **most preferred interview solution**

         ```python
         def moveZeroes(nums):
            k = 0

            for i in range(len(nums)):
               if nums[i] != 0:
                     nums[i], nums[k] = nums[k], nums[i]
                     k += 1
         ```

         ---

         ## 🔥 Why This Is Best

         * Single loop → cleaner
         * In-place swaps
         * Maintains order automatically

         ---

         ## ⏱ Complexity

         * **Time:** O(n)
         * **Space:** O(1)

         ---

         # 🧠 Interview Summary

         | Approach     | Time | Space | In-Place |
         | ------------ | ---- | ----- | -------- |
         | Your (Brute) | O(n) | O(n)  | ❌ No     |
         | Optimized    | O(n) | O(1)  | ✅ Yes    |
         | Swap (Best)  | O(n) | O(1)  | ✅ Yes    |

         ---

         # 🎯 Key Insight (Say this in interview)

         > “Instead of using extra space, we can track the position of the next non-zero element and overwrite the array in-place.”

         ---


4. Longest Substring Without Repeating Characters
   → LeetCode: *Longest Substring Without Repeating Characters*
   Given a string s, find the length of the longest substring without duplicate characters.
            Example 1:

            Input: s = "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
            Example 2:

            Input: s = "bbbbb"
            Output: 1
            Explanation: The answer is "b", with the length of 1.
            Example 3:

            Input: s = "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3.
            Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
         
         Your solution is actually **not brute force** — it’s a **sliding window approach**, but implemented with a **list**, which makes it slower than optimal. Let’s analyze it properly 👇

         ---

         # 🔴 Your Code Analysis

         ```python
         list1 = []
         for i in s:
            if i not in list1:
               list1.append(i)
            else:
               t = list1.index(i)
               del list1[:t+1]
               list1.append(i)
         ```

         ---

         ## ⏱ Time Complexity

         Let `n = len(s)`

         ### Key operations inside loop:

         1. `i not in list1` → O(n)
         2. `list1.index(i)` → O(n)
         3. `del list1[:t+1]` → O(n)

         👉 Each iteration can take **O(n)** in worst case

         ### Total:

         ```
         O(n) * O(n) = O(n²)
         ```

         ❌ **Time Complexity = O(n²)**

         ---

         ## 📦 Space Complexity

         * `list1` stores unique characters
         * In worst case (all unique):

         ```
         O(n)
         ```

         ✅ **Space Complexity = O(n)**

         ---

         # ⚠️ Why This Is Slow

         * You're using a **list**
         * Membership check + index search = **linear time**
         * That’s why it becomes O(n²)

         ---

         # 🟢 Optimized Solution (Sliding Window + HashMap)

         ## 💡 Idea

         * Use a **dictionary (hashmap)** to store last seen index
         * Move left pointer efficiently (no deletion needed)

         ---

         ## 💻 Code (Best Approach)

         ```python
         def lengthOfLongestSubstring(s):
            char_map = {}
            left = 0
            max_length = 0

            for right in range(len(s)):
               if s[right] in char_map:
                     left = max(left, char_map[s[right]] + 1)

               char_map[s[right]] = right
               max_length = max(max_length, right - left + 1)

            return max_length
         ```

         ---

         ## 🔁 Example Walkthrough

         ```
         s = "abcabcbb"
         ```

         | Right | Char | Left | Window | Length |
         | ----- | ---- | ---- | ------ | ------ |
         | 0     | a    | 0    | a      | 1      |
         | 1     | b    | 0    | ab     | 2      |
         | 2     | c    | 0    | abc    | 3      |
         | 3     | a    | 1    | bca    | 3      |
         | 4     | b    | 2    | cab    | 3      |

         👉 Answer = **3**

         ---

         ## ⏱ Time Complexity

         * Each character processed **once**
         * `left` only moves forward

         ```
         O(n)
         ```

         ✅ **Time Complexity = O(n)**

         ---

         ## 📦 Space Complexity

         * Hashmap stores characters

         ```
         O(min(n, charset))
         ```

         👉 For ASCII → O(1)
         👉 General → O(n)

         ---

         # 🔥 Why This Is Optimal

         | Operation | List (Your Code) | HashMap |
         | --------- | ---------------- | ------- |
         | Search    | O(n) ❌           | O(1) ✅  |
         | Update    | O(n) ❌           | O(1) ✅  |

         ---

         # 🧠 Interview Insight (IMPORTANT)

         Say this:

         > “Using a list makes membership checks O(n), so we optimize using a hashmap to achieve O(1) lookup, reducing total complexity to O(n).”

         ---

         # 🚀 Bonus (Even Cleaner Version using set)

         ```python
         def lengthOfLongestSubstring(s):
            char_set = set()
            left = 0
            max_length = 0

            for right in range(len(s)):
               while s[right] in char_set:
                     char_set.remove(s[left])
                     left += 1

               char_set.add(s[right])
               max_length = max(max_length, right - left + 1)

            return max_length
         ```

         ---

         ## Comparison

         | Approach  | Time  | Space |
         | --------- | ----- | ----- |
         | Your Code | O(n²) | O(n)  |
         | HashMap   | O(n)  | O(n)  |
         | Set       | O(n)  | O(n)  |




5. Valid Anagram
   → LeetCode: *Valid Anagram*

👉 Concepts:

* Hashing
* Sliding Window
* Two pointers

---
         

## 🔹 2. Sorting + Searching

**Questions:**

1. Binary Search
   → LeetCode: *Binary Search*

2. Search in Rotated Sorted Array
   → LeetCode: *Search in Rotated Sorted Array*

3. Kth Largest Element
   → LeetCode: *Kth Largest Element in an Array*

👉 Concepts:

* Binary Search
* Heap / Priority Queue

---

## 🔹 3. Linked List

**Questions:**

1. Reverse Linked List
   → LeetCode: *Reverse Linked List*

2. Detect Cycle
   → LeetCode: *Linked List Cycle*

3. Merge Two Sorted Lists
   → LeetCode: *Merge Two Sorted Lists*

👉 Concepts:

* Fast & slow pointer
* Pointer manipulation

---

## 🔹 4. Stack & Queue

**Questions:**

1. Valid Parentheses
   → LeetCode: *Valid Parentheses*

2. Min Stack
   → LeetCode: *Min Stack*

3. Implement Queue using Stacks
   → LeetCode: *Implement Queue using Stacks*

---

## 🔹 5. Recursion + Backtracking (Basic)

**Questions:**

1. Subsets
   → LeetCode: *Subsets*

2. Permutations
   → LeetCode: *Permutations*

---

## 🔹 6. Basic Trees

**Questions:**

1. Inorder Traversal
   → LeetCode: *Binary Tree Inorder Traversal*

2. Maximum Depth of Binary Tree
   → LeetCode: *Maximum Depth of Binary Tree*

3. Level Order Traversal
   → LeetCode: *Binary Tree Level Order Traversal*

---

## 🔹 7. Basic Dynamic Programming

**Questions:**

1. Climbing Stairs
   → LeetCode: *Climbing Stairs*

2. House Robber
   → LeetCode: *House Robber*

👉 Concepts:

* Memoization
* Tabulation

---

# 🧠 PHASE 2: MNCs (Google, Microsoft, Amazon)

👉 Focus:

* **Deep problem solving**
* **Optimization**
* **Multiple approaches**

---

## 🔥 1. Advanced Arrays & Sliding Window

**Questions:**

1. Trapping Rain Water
   → LeetCode: *Trapping Rain Water*

2. Maximum Sliding Window
   → LeetCode: *Sliding Window Maximum*

3. Product of Array Except Self
   → LeetCode: *Product of Array Except Self*

---

## 🔥 2. Advanced Binary Search

**Questions:**

1. Median of Two Sorted Arrays (🔥 Google favorite)
   → LeetCode: *Median of Two Sorted Arrays*

2. Find Peak Element
   → LeetCode: *Find Peak Element*

---

## 🔥 3. Graphs (VERY IMPORTANT)

**Questions:**

1. Number of Islands
   → LeetCode: *Number of Islands*

2. Course Schedule
   → LeetCode: *Course Schedule*

3. Clone Graph
   → LeetCode: *Clone Graph*

4. Dijkstra / Shortest Path
   → LeetCode: *Network Delay Time*

👉 Concepts:

* BFS / DFS
* Topological sort
* Union-Find

---

## 🔥 4. Trees (Advanced)

**Questions:**

1. Lowest Common Ancestor
   → LeetCode: *Lowest Common Ancestor of Binary Tree*

2. Serialize and Deserialize Binary Tree
   → LeetCode: *Serialize and Deserialize Binary Tree*

3. Binary Tree Maximum Path Sum
   → LeetCode: *Binary Tree Maximum Path Sum*

---

## 🔥 5. Dynamic Programming (CORE OF MNCs)

**Questions:**

1. Longest Increasing Subsequence
   → LeetCode: *Longest Increasing Subsequence*

2. Coin Change
   → LeetCode: *Coin Change*

3. Edit Distance (🔥 Microsoft favorite)
   → LeetCode: *Edit Distance*

4. Longest Common Subsequence
   → LeetCode: *Longest Common Subsequence*

---

## 🔥 6. Backtracking (Hard Level)

**Questions:**

1. N-Queens
   → LeetCode: *N-Queens*

2. Word Search
   → LeetCode: *Word Search*

---

## 🔥 7. Heap / Greedy

**Questions:**

1. Merge K Sorted Lists
   → LeetCode: *Merge k Sorted Lists*

2. Top K Frequent Elements
   → LeetCode: *Top K Frequent Elements*

