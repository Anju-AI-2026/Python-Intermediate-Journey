# Running Sum of 1D Array

A Python solution to LeetCode Problem 1480 that calculates the running sum of an array using a loop and a separate result list.

## Problem Description

Given an array of integers `nums`, calculate the running sum of the array.

The running sum at each position is the sum of all elements from the beginning of the array up to that position.

## Example

**Input:**
```python
nums = [1, 2, 3, 4]
```

**Output:**
```text
[1, 3, 6, 10]
```

**Explanation:**

- First element: 1
- Second element: 1 + 2 = 3
- Third element: 1 + 2 + 3 = 6
- Fourth element: 1 + 2 + 3 + 4 = 10

## Concepts Practiced

- Python lists
- `for` loops
- Accumulator variables
- List `append()` method
- Functions and return values
- Sequential data processing

## How It Works

1. An empty list named `result` stores the running sums.
2. A variable named `total` is initialized to zero.
3. The program iterates through each number in `nums`.
4. Each number is added to `total`.
5. The updated total is appended to `result`.
6. After processing all elements, the function returns the result list.

## Time and Space Complexity

- **Time Complexity:** O(n) – Each element is processed once.
- **Space Complexity:** O(n) – A new result list stores the cumulative sums.

## Purpose

To practice loops, accumulator variables, and list operations while learning how to calculate cumulative sums efficiently.