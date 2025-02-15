# Best Time to Buy and Sell Stock

Leet Code reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Topic: Array, Greedy Approach

## Description

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to 
sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


**Example 1:**

    Input: prices = [7,1,5,3,6,4]
    Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

    Input: prices = [7,6,4,3,1]
    Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

- 1 <= prices.length <= 105
- 0 <= prices[i] <= 104

## Visualisation

![121_best_time_to_buy_and_sell_stock.png](..%2Fimages%2F121_best_time_to_buy_and_sell_stock.png)

## Additional notes

The optimal approach uses a single pass with a greedy algorithm to achieve O(n) time complexity and O(1) space 
complexity.

At every step, we keep track of the minimum buy price of stock encountered so far. For every price, we subtract 
with the minimum so far and if we get more profit than the current result, we update the result.

This algorithm is called greedy because it makes locally optimal choices at each step with the hope that these 
choices lead to a globally optimal solution.

Greedy Approach in This Algorithm:
- Tracking the Minimum Price So Far
- Maximizing Profit at Every Step
- No Backtracking: Unlike dynamic programming, which may explore multiple solutions and backtrack, the greedy approach 
only looks forward.