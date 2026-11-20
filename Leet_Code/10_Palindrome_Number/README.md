# Palindrome Number

A Python solution to LeetCode Problem 9 that checks whether an integer reads the same forward and backward without converting it into a string.

## Problem Description

Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

A palindrome number reads the same forward and backward.

## Examples

**Example 1:**

Input:
```python
x = 121
```

Output:
```text
True
```

**Example 2:**

Input:
```python
x = -121
```

Output:
```text
False
```

**Example 3:**

Input:
```python
x = 10
```

Output:
```text
False
```

## Concepts Practiced

- Python classes and methods
- Type hints
- `if` conditions
- `while` loops
- Modulus operator (`%`)
- Floor division (`//`)
- Reversing a number mathematically

## How It Works

1. If the number is negative, return `False`.
2. Store the original number in `original`.
3. Initialize `reversed_number` to zero.
4. Use a `while` loop to extract the last digit using the modulus operator.
5. Build the reversed number by multiplying the current result by 10 and adding the extracted digit.
6. Remove the last digit from `x` using floor division.
7. Compare the original number with the reversed number.
8. Return the comparison result.

## Time and Space Complexity

- **Time Complexity:** O(log n) – Each iteration processes one digit of the number.
- **Space Complexity:** O(1) – Only a fixed number of variables are used.

## Purpose

To practise mathematical operations, loops, and number manipulation while learning how to check palindromes without string conversion.