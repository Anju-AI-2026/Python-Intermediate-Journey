# Move Zeroes

A Python solution to LeetCode Problem 283 that moves all zeroes to the end of an array while maintaining the relative order of non-zero elements.

## Problem Description

Given an integer array `nums`, move all zeroes to the end of it while maintaining the relative order of the non-zero elements.

The operation must be performed in-place.

## Example

**Input:**
```python
numbers = [0, 1, 0, 3, 12]
```

**Output:**
```text
[1, 3, 12, 0, 0]
```

## Concepts Practiced

- Python lists
- Classes and methods
- `for` loops
- `while` loops
- Conditional statements
- In-place array modification
- Index-based operations

## How It Works

1. Initialize `position` to zero to track where the next non-zero number should be placed.
2. Iterate through each number in the list.
3. If the number is not zero, place it at the current `position`.
4. Increase `position` after placing each non-zero number.
5. Use a `while` loop to fill the remaining positions with zeroes.
6. The original list is modified directly.

## Time and Space Complexity

- **Time Complexity:** O(n) – The list is traversed to move non-zero elements and fill the remaining positions.
- **Space Complexity:** O(1) – The operation modifies the original list without creating another list.

## Purpose

To practise in-place array modification, loops, and index management while learning how to move elements efficiently.