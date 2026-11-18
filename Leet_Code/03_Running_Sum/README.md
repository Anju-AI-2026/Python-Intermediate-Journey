# Running Sum of 1d Array

**LeetCode Problem:** #1480

## Problem Description

Given an array of numbers, return an array where each element is the sum of all elements from the beginning up to that position.

## Example

**Input:** `[1, 2, 3, 4]`

**Output:** `[1, 3, 6, 10]`

## Concepts Used

- Python classes and methods
- Lists
- `for` loops
- Running totals
- `append()`
- `return`

## How It Works

1. Create an empty list named `result`.
2. Initialize `total` to zero.
3. Iterate through each number in the input list.
4. Add the current number to `total`.
5. Append the updated total to `result`.
6. Return the completed result list.

## Time and Space Complexity

- **Time Complexity:** O(n) — Each element is visited once.
- **Space Complexity:** O(n) — A result list stores the running sums.

## Learning Purpose

To practise list operations, loops, and maintaining a cumulative total while processing an array.