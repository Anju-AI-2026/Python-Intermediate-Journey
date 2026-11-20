# Majority Element

A Python solution to LeetCode Problem 169 that finds the majority element in an array using the Boyer-Moore Voting Algorithm.

## Problem Description

Given an array `nums` of size `n`, find the majority element.

The majority element is the element that appears more than `n // 2` times in the array.

You may assume that the majority element always exists.

## Examples

**Example 1:**

Input:
```python
nums = [3, 2, 3]
```

Output:
```text
3
```

**Example 2:**

Input:
```python
nums = [2, 2, 1, 1, 1, 2, 2]
```

Output:
```text
2
```

## Concepts Practiced

- Python classes and methods
- Lists and type hints
- `for` loops
- Conditional statements
- Candidate selection
- Counting occurrences
- Boyer-Moore Voting Algorithm

## How It Works

1. Initialize `count` to zero and `candidate` to `None`.
2. Iterate through each number in the array.
3. If `count` is zero, select the current number as the candidate.
4. If the current number matches the candidate, increase the count.
5. Otherwise, decrease the count.
6. After processing all elements, return the candidate.

## Time and Space Complexity

- **Time Complexity:** O(n) – Each element is visited once.
- **Space Complexity:** O(1) – Only two extra variables are used.

## Purpose

To understand the Boyer-Moore Voting Algorithm and practise solving array problems using efficient candidate tracking.