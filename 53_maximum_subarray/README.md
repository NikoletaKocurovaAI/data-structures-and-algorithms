# Maximum Subarray

Leet Code reference: https://leetcode.com/problems/maximum-subarray/description/

Topic: Array, Divide and Conquer

## Description

Given an integer array nums, find the subarray with the largest sum, and return its sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Visualisation

![53_subarray.png](..%2Fimages%2F53_subarray.png)

## Additional notes

**Kadane's Algorithm**

It keeps track of:
- The current maximum subarray sum ending at the current element (current_sum).
- The global maximum sum found so far (max_sum).

It dynamically decides:

- Extend the current subarray: When adding the current element improves the sum.
- Start a new subarray: When the current element alone is larger than the previous subarray sum.

O(n) time, O(1) space

**Divide and conquer approach**

This approach splits the array into halves, solves each half recursively, and combines the results to find the global maximum.

The given solution is not dynamic programming. Algorithm is not greedy.

**Dynamic programming**

Breaking the problem into smaller subproblems and solving each subproblem only once while reusing its result.

**Memoization** is a dynamic programming technique where the results of already-solved subproblems are stored in 
a table (often a dictionary or array) so that they can be reused later, avoiding redundant computations. 