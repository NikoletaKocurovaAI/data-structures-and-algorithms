# Climbing stairs

Leet Code reference: https://leetcode.com/problems/climbing-stairs

Topic: Math, Dynamic Programming & Memoization

## Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:**

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

**Example 2:**

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

## Visualisation

xx

**Dynamic programming**

Breaking the problem into smaller subproblems and solving each subproblem only once while reusing its result.

We can cache previously computed values using memoization to avoid redundant calculations. This technique is called 
Dynamic Programming (Top-Down Approach).

How Memoization Works

**Memoization** is a dynamic programming technique where the results of already-solved subproblems are stored in 
a table (often a dictionary or array) so that they can be reused later, avoiding redundant computations. 

Instead of recalculating f(n) multiple times, we store the results in a dictionary (or an array) and reuse them. This 
reduces the time complexity from O(2^n) to O(n).

## Additional notes

This is a classic Dynamic Programming (DP) problem that follows the Fibonacci sequence.

To reach the nth step, you could have come from:
- The (n−1)th step by taking one step.
- The (n−2)th step by taking two steps.

Thus, the recurrence relation is: **f(n)=f(n−1)+f(n−2)**, where:
- f(1)=1 (only one way: taking one step)
- f(2)=2 (either take two 1-steps or one 2-step)

Approaches:
- Recursive Approach (Brute Force) - Backtracking
Time Complexity: exponential O(2ⁿ)
Space Complexity: O(n) (call stack)
Recursive Approach? Yes.

- Dynamic Programming with Memoization (Top-Down) 
Time Complexity: O(n), 
Space Complexity: O(n) (for memoization)
Recursive Approach? Yes.

- Dynamic Programming with Tabulation (Bottom-Up) 
Time Complexity: O(n)
Space Complexity: O(n) (array)
Recursive Approach? No.

- Optimized Fibonacci with Constant Space
Time Complexity: O(n), 
Space Complexity: O(1) (optimal, constant space)
Recursive Approach? No.

To explicitly generate all possible ways to climb the staircase (rather than just counting them), we need 
a backtracking or recursion-based approach that constructs all the valid paths.

This problem follows the combination principle rather than permutation.

Example for n=4. Which matches the Fibonacci approach!
- When 4 ones and 0 twos, then [1,1,1,1] → C(4,0)=1.
- When 2 ones and 1 twos, then [2,1,1], [1,2,1], [1,1,2] → C(3,1)=3
- When 0 ones and 2 twos, then [2,2] → C(2,2)=1
When 4 ones and 0 twos, then C(2,2),

