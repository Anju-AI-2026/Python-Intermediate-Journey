# Two Sum

A Python solution to the LeetCode Two Sum problem using a dictionary and the `enumerate()` function.

## Problem Description

Given a list of integers `nums` and an integer `target`, find the indices of two numbers whose sum equals the target.

The solution returns the indices of the two numbers.

## Example

**Input:**
```python
nums = [2, 7, 11, 15]
target = 9
```

**Output:**
```text
[0, 1]
```

**Explanation:**

The numbers `2` and `7` add up to `9`. Their indices are `0` and `1`.

## Concepts Practiced

- Python dictionaries
- `enumerate()` function
- `for` loops
- Conditional statements
- Dictionary membership using `in`
- Functions and return values
- Index-based data processing

## How It Works

1. An empty dictionary named `seen` stores previously visited numbers and their indices.
2. `enumerate(nums)` provides each number along with its index.
3. The `difference` variable calculates the number needed to reach the target.
4. The program checks whether the difference already exists in `seen`.
5. If found, the function returns the stored index and the current index.
6. Otherwise, the current number and its index are added to the dictionary.

## Time and Space Complexity

- **Time Complexity:** O(n) – The list is traversed once, and dictionary lookups take O(1) average time.
- **Space Complexity:** O(n) – The dictionary may store up to all elements.

## Purpose

To practice dictionary-based problem solving, efficient searching, and using `enumerate()` to work with both values and indices.