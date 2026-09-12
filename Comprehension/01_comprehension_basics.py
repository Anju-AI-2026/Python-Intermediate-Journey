# Python List Comprehensions
# This file contains basic list comprehension examples.


# Program 1: Create squares of numbers from 1 to 10
# Demonstrates transformation using a list comprehension.

numbers = range(1, 11)

squares = [num * num for num in numbers]

print("Squares:", squares)


# Program 2: Select even numbers
# Demonstrates filtering using a condition.

numbers = [12, 7, 4, 9, 16, 3, 20, 11]

even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers:", even_numbers)


# Program 3: Select odd numbers
# Demonstrates filtering with a different condition.

numbers = [12, 7, 4, 9, 16, 3, 20, 11]

odd_numbers = [num for num in numbers if num % 2 != 0]

print("Odd numbers:", odd_numbers)


# Program 4: Convert names to uppercase
# Demonstrates transforming strings inside a list.

names = ["anjali", "riya", "sara", "meena"]

uppercase_names = [name.upper() for name in names]

print("Uppercase names:", uppercase_names)