# Search Insert Position

A Python solution to LeetCode Problem 35 that finds the index of a target value in a sorted array or determines where it should be inserted using binary search.

## Problem Description

Given a sorted array of distinct integers `nums` and a target value, return the index if the target is found.

If the target is not found, return the index where it would be inserted to maintain the sorted order.

The solution must use O(log n) time complexity.

## Examples

**Example 1:**

Input:
```python
nums = [1, 3, 5, 6]
target = 5
```

Output:
```text
2
```

**Example 2:**

Input:
```python
nums = [1, 3, 5, 6]
target = 2
```

Output:
```text
1
```

**Example 3:**

Input:
```python
nums = [1, 3, 5, 6]
target = 7
```

Output:
```text
4
```

## Concepts Practiced

- Python classes and methods
- Lists and type hints
- Binary search
- `while` loops
- Conditional statements
- Index manipulation
- Integer division using `//`

## How It Works

1. Initialize `left` to the first index and `right` to the last index.
2. Continue searching while `left` is less than or equal to `right`.
3. Calculate the middle index using integer division.
4. If the middle element equals the target, return its index.
5. If the middle element is smaller than the target, search the right half.
6. Otherwise, search the left half.
7. If the target is not found, return `left`, which represents the correct insertion position.

## Time and Space Complexity

- **Time Complexity:** O(log n) – The search space is reduced by half in each iteration.
- **Space Complexity:** O(1) – Only a fixed number of variables are used.

## Purpose

To practise binary search and understand how to efficiently locate elements or insertion positions in a sorted array.