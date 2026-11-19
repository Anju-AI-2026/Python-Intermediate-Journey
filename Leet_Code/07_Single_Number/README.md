# Single Number

A Python solution to LeetCode Problem 136 that finds the element that appears only once in an array using the XOR bitwise operator.

## Problem Description

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single element.

## Examples

**Example 1:**

Input:
```python
nums = [4, 1, 2, 1, 2]
```

Output:
```text
4
```

**Example 2:**

Input:
```python
nums = [2, 2, 1]
```

Output:
```text
1
```

## Concepts Practiced

- Python classes and methods
- Lists
- `for` loops
- Bitwise XOR operator (`^`)
- Variable accumulation
- Functions and return values

## How It Works

1. Initialize `result` to zero.
2. Iterate through every number in the list.
3. Apply the XOR operator between `result` and the current number.
4. Repeated numbers cancel each other out because XOR of a number with itself is zero.
5. The remaining value is the number that appears only once.
6. Return `result`.

## Time and Space Complexity

- **Time Complexity:** O(n) – Each element is processed once.
- **Space Complexity:** O(1) – Only one extra variable is used.

## Purpose

To understand the bitwise XOR operator and practise solving array problems efficiently using bit manipulation.