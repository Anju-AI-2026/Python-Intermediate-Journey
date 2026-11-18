# Two Sum

**LeetCode Problem:** #1

## Problem Description

Given an array of integers and a target value, find the indices of two numbers whose sum equals the target.

## Example

**Input:**
- Numbers: `[2, 7, 11, 15]`
- Target: `9`

**Expected Output:** `[0, 1]`

## Concepts Used

- Python classes and methods
- Dictionaries
- `enumerate()`
- Loops and conditional statements
- Key-value pairs

## How It Works

1. Create an empty dictionary named `seen`.
2. Iterate through the numbers using `enumerate()` to get each number and its index.
3. Calculate the difference between the target and the current number.
4. Check whether that difference already exists in the dictionary.
5. If it exists, return the two indices.
6. Otherwise, store the current number and its index in the dictionary.

## Time and Space Complexity

- **Time Complexity:** O(n) — Each element is visited once.
- **Space Complexity:** O(n) — The dictionary stores numbers and their indices.

## Learning Purpose

To practise dictionary operations and learn how to solve the Two Sum problem efficiently using a hash map.