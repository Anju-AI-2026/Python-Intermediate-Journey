# Python Comprehensions with Conditions
# This file contains filtering and if-else examples.


# Program 1: Select passing marks
# Demonstrates filtering values using a condition.

marks = [35, 78, 42, 29, 90, 56, 38, 40]

passed_marks = [mark for mark in marks if mark >= 40]

print("Passed marks:", passed_marks)


# Program 2: Add 18% tax to prices
# Demonstrates transforming floating-point values.

prices = [100.0, 250.5, 80.0, 125.75]

final_prices = [price * 1.18 for price in prices]

print("Final prices:", final_prices)


# Program 3: Classify marks as Pass or Fail
# Demonstrates if-else inside a list comprehension.

marks = [35, 78, 42, 29, 90, 56, 38, 40]

pass_fail = ["Pass" if mark >= 40 else "Fail" for mark in marks]

print("Results:", pass_fail)


# Program 4: Classify numbers as Positive, Negative, or Zero
# Demonstrates multiple conditions inside a list comprehension.

numbers = [12, -5, 0, 8, -2, 0, 15]

number_types = [
    "Zero" if num == 0
    else "Positive" if num > 0
    else "Negative"
    for num in numbers
]

print("Number types:", number_types)