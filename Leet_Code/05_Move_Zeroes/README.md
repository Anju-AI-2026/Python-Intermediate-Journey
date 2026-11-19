# Valid Anagram

A Python solution to LeetCode Problem 242 that checks whether two strings are anagrams using `Counter` from the `collections` module.

## Problem Description

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

Two strings are anagrams if they contain the same characters with the same frequency, but the characters can appear in a different order.

- Return `True` if the strings are anagrams.
- Return `False` otherwise.

## Examples

**Example 1:**

Input:
```python
s = "anagram"
t = "nagaram"
```

Output:
```text
True
```

**Example 2:**

Input:
```python
s = "rat"
t = "car"
```

Output:
```text
False
```

## Concepts Practiced

- Python strings
- `collections` module
- `Counter` class
- String length using `len()`
- Conditional statements
- Functions and return values
- Comparing character frequencies

## How It Works

1. The `Counter` class is imported from the `collections` module.
2. The `isAnagram()` function receives two strings.
3. It first compares their lengths. If the lengths differ, it returns `False`.
4. `Counter(s)` counts the frequency of each character in the first string.
5. `Counter(t)` counts the frequency of each character in the second string.
6. Both counters are compared. If they are equal, the function returns `True`; otherwise, it returns `False`.

## Time and Space Complexity

- **Time Complexity:** O(n) – Counting and comparing character frequencies takes linear time.
- **Space Complexity:** O(n) – The counters store character-frequency information.

## Purpose

To understand character frequency analysis and practice using Python's `Counter` class to solve string-related problems efficiently.