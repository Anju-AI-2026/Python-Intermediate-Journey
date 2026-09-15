# Square numbers using map()
def double(num):
    return num * num

numbers = [2, 4, 6, 8]

square = list(map(double, numbers))

print(square)


# Get the length of each name
def get_length(name):
    return len(name)

names = ["anju", "rossy", "ai", "python"]

new_list = list(map(get_length, names))

print(new_list)


# Add 10% tax to each price
def add_tax(price):
    return price * 1.10

prices = [100, 250, 500, 750]

new_price = list(map(add_tax, prices))

print(new_price)


# Find the cube of each number
def get_cube(num):
    return num * num * num

numbers = [1, 2, 3, 4, 5]

cubed = list(map(get_cube, numbers))

print(cubed)


# Convert names to uppercase
def uppercase(name):
    return name.upper()

names = ["anju", "rossy", "python", "ai"]

uppercase_list = list(map(uppercase, names))

print(uppercase_list)