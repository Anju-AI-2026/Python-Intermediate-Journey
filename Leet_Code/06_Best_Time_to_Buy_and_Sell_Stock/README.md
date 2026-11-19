# Best Time to Buy and Sell Stock

A Python solution to LeetCode Problem 121 that finds the maximum profit possible from buying and selling a stock.

## Problem Description

Given an array `prices` where `prices[i]` represents the price of a stock on the ith day, find the maximum profit that can be achieved by buying on one day and selling on a future day.

If no profit is possible, return `0`.

## Examples

**Example 1:**

Input:
```python
prices = [7, 1, 5, 3, 6, 4]
```

Output:
```text
5
```

**Example 2:**

Input:
```python
prices = [7, 6, 4, 3, 1]
```

Output:
```text
0
```

## Concepts Practiced

- Python classes and methods
- Lists
- `for` loops
- Conditional statements
- Minimum value tracking
- Maximum profit calculation
- Greedy approach

## How It Works

1. Initialize `minimum_price` with the first stock price.
2. Initialize `maximum_profit` to zero.
3. Iterate through each price in the list.
4. If the current price is lower than `minimum_price`, update it.
5. Calculate the possible profit using the current price and minimum price.
6. If the calculated profit is greater than `maximum_profit`, update it.
7. Return the maximum profit.

## Time and Space Complexity

- **Time Complexity:** O(n) – Each stock price is processed once.
- **Space Complexity:** O(1) – Only a fixed number of variables are used.

## Purpose

To practise array traversal, tracking minimum and maximum values, and applying a greedy approach to solve stock-related problems.