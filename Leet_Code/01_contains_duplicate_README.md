# Contains Duplicate – List-Based Approach

A Python solution to check whether a list contains any duplicate numbers using a separate list to track previously visited elements.

## Problem Description

Given a list of numbers, determine whether any number appears more than once.

- Return `True` if a duplicate exists.
- Return `False` if all numbers are unique.

## Example

**Input:**
```python
numbers = [1, 2, 3, 4]
```

**Output:**
```text
False
```

## Concepts Practiced

- Python lists
- `for` loops
- Conditional statements
- List membership using `in`
- Functions and return values
- Tracking previously visited elements

## How It Works

1. The `numbers` list stores the input values.
2. An empty list named `new_num` stores numbers that have already been checked.
3. The `seen_num()` function iterates through the input list.
4. If the current number already exists in `new_num`, the function returns `True`.
5. Otherwise, the number is added to `new_num`.
6. If the loop finishes without finding a duplicate, the function returns `False`.

## Time and Space Complexity

- **Time Complexity:** O(n²) in the worst case because checking membership in a list takes linear time.
- **Space Complexity:** O(n) because a separate list stores previously visited numbers.

## Purpose

To practice duplicate detection using Python lists, loops, functions, and membership operators.