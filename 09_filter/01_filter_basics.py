# Filter numbers greater than 20
numbers = [10, 15, 20, 25, 30, 35]

def true_num(num):
    if num > 20:
        return True

new_list = list(filter(true_num, numbers))

print(new_list)


# Filter even numbers
numbers = [3, 8, 11, 14, 17, 20, 23]

def is_even(num):
    if num % 2 == 0:
        return True

even_numbers = list(filter(is_even, numbers))

print(even_numbers)


# Filter names with more than 4 characters
names = ["Anju", "Rossy", "Python", "AI", "Developer"]

def true_name(name):
    if len(name) > 4:
        return True

new_names = list(filter(true_name, names))

print(new_names)


# Filter prices within a specific range
prices = [50, 120, 80, 250, 300, 90]

def check_price(price):
    if price >= 80 and price <= 250:
        return True

new_prices = list(filter(check_price, prices))

print(new_prices)


# Filter non-empty words
words = ["apple", "", "python", "", "AI", "developer"]

def is_empty(name):
    if len(name) != 0:
        return True

new_words = list(filter(is_empty, words))

print(new_words)