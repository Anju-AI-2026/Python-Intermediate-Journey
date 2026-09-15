# Filter positive numbers divisible by 3
numbers = [-9, 6, -4, 12, 15, -18, 7, 21, 0]

def is_true(num):
    if num % 3 == 0 and num > 0:
        return True

new_numbers = list(filter(is_true, numbers))

print(new_numbers)


# Filter names starting with A or P
names = ["Anju", "Ramesh", "AI", "Python", "Rossy", "ML"]

def start_with(name):
    if name.startswith("A") or name.startswith("P"):
        return True

start_with_name = list(filter(start_with, names))

print(start_with_name)


# Filter words containing the letter 'a'
words = ["apple", "banana", "kiwi", "avocado", "mango", "orange"]

def has_a(word: str):
    if "a" in word:
        return True

has_a_words = list(filter(has_a, words))

print(has_a_words)


# Filter students with marks of 60 or above
students = [
    {"name": "Anju", "marks": 85},
    {"name": "Ravi", "marks": 42},
    {"name": "Rossy", "marks": 91},
    {"name": "Meena", "marks": 58},
    {"name": "Arjun", "marks": 76}
]

def mark_check(student):
    if student["marks"] >= 60:
        return True

new_students = list(filter(mark_check, students))

print(new_students)


# Filter numbers with an even last digit
numbers = [10, 21, 32, 43, 54, 65, 76, 87]

def last_digit(num):
    new_num = num % 10
    if new_num % 2 == 0:
        return True

last_num = list(filter(last_digit, numbers))

print(last_num)