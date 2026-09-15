# Filter numbers divisible by 4 using lambda
numbers = [5, 12, 7, 20, 33, 40, 18]

new_num = list(filter(lambda num: num % 4 == 0, numbers))

print(new_num)


# Filter words with 4 or more characters using lambda
words = ["python", "AI", "developer", "ML", "machine", "code"]

new_word = list(filter(lambda word: len(word) >= 4, words))

print(new_word)


# Filter prices that are not divisible by 3 using lambda
prices = [99, 150, 249, 300, 450, 75, 600]

new_price = list(filter(lambda price: price % 3 != 0, prices))

print(new_price)


# Filter students with marks above 75 using lambda
students = [
    {"name": "Anju", "marks": 85},
    {"name": "Ravi", "marks": 42},
    {"name": "Rossy", "marks": 91},
    {"name": "Meena", "marks": 58},
    {"name": "Arjun", "marks": 76}
]

new_data = list(filter(lambda student: student["marks"] > 75, students))

print(new_data)


# Filter words ending with 'ing' using lambda
words = [
    "coding",
    "python",
    "learning",
    "AI",
    "testing",
    "developer",
    "building"
]

new_word_data = list(filter(lambda word: word.endswith("ing"), words))

print(new_word_data)