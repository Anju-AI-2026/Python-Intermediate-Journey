# Contains Duplicate

**LeetCode Problem:** #217

A Python solution to determine whether an array contains any duplicate elements using a set.

## Problem Description

Given an integer array `nums`, return `True` if any value appears at least twice. Return `False` if every element is distinct.

## Example

**Input:**
```python
nums = [1, 2, 3, 1]
```

**Output:**
```text
True
```

**Explanation:** The number `1` appears more than once.

## Concepts Practiced

- Python sets
- Loops and conditional statements
- Membership checking using `in`
- Functions and return values
- Duplicate detection

## How It Works

1. Create an empty set named `seen`.
2. Iterate through each number in the array.
3. Check whether the number already exists in the set.
4. If it exists, return `True`.
5. Otherwise, add the number to the set.
6. If no duplicate is found, return `False`.

## Complexity Analysis

- **Time Complexity:** O(n) average time.
- **Space Complexity:** O(n) in the worst case.

## Purpose

To practise set operations and efficient duplicate detection in Python.