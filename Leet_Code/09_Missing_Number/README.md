# Missing Number

A Python solution to LeetCode Problem 268 that finds the missing number in an array using the mathematical sum formula.

## Problem Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, find the one number that is missing from the array.

## Examples

**Example 1:**

Input:
```python
nums = [3, 0, 1]
```

Output:
```text
2
```

**Example 2:**

Input:
```python
nums = [0, 1]
```

Output:
```text
2
```

**Example 3:**

Input:
```python
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
```

Output:
```text
8
```

## Concepts Practiced

- Python classes and methods
- Lists and type hints
- `len()` function
- `sum()` function
- Arithmetic operations
- Mathematical formulas
- Integer division using `//`

## How It Works

1. Find the length of the array and store it in `n`.
2. Calculate the expected sum of all numbers from `0` to `n`.
3. Calculate the actual sum of the numbers in the given array.
4. Subtract the actual sum from the expected sum.
5. Return the difference, which is the missing number.

## Time and Space Complexity

- **Time Complexity:** O(n) – The `sum()` function processes each element once.
- **Space Complexity:** O(1) – Only a fixed number of extra variables are used.

## Purpose

To practise mathematical problem-solving and understand how arithmetic formulas can be used to solve array problems efficiently.