# Contains Duplicate – Set-Based Approach

A Python solution to LeetCode Problem 217 (Contains Duplicate) using a set to efficiently identify repeated elements.

## Problem Description

Given a list of integers `nums`, determine whether any value appears at least twice.

- Return `True` if a duplicate exists.
- Return `False` if every element is unique.

## Example

**Input:**
```python
nums = [1, 2, 3, 1]
```

**Output:**
```text
True
```

**Explanation:**

The number `1` appears more than once in the list.

## Concepts Practiced

- Python sets
- `for` loops
- Conditional statements
- Set membership using `in`
- `set.add()` method
- Functions and return values
- Duplicate detection

## How It Works

1. An empty set named `seen` is created to store visited numbers.
2. The program iterates through each number in `nums`.
3. It checks whether the current number already exists in `seen`.
4. If the number exists, the function immediately returns `True`.
5. Otherwise, the number is added to the set using `seen.add(num)`.
6. If the loop finishes without finding a duplicate, the function returns `False`.

## Time and Space Complexity

- **Time Complexity:** O(n) – Each number is processed once, and set membership checking takes O(1) average time.
- **Space Complexity:** O(n) – The set may store all elements if no duplicates exist.

## Purpose

To understand how Python sets can improve searching efficiency and solve duplicate detection problems with better average-time performance than a list-based approach.