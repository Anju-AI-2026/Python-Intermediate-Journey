# Double numbers using lambda and map()
numbers = [2, 4, 6, 8]

new_number = list(map(lambda num: num * 2, numbers))

print(new_number)


# Add 10 to each number using lambda
numbers = [1, 2, 3, 4, 5]

add_ten = list(map(lambda num: num + 10, numbers))

print(add_ten)


# Divide each number by 5 using lambda
numbers = [5, 10, 15, 20]

divide_num = list(map(lambda num: num / 5, numbers))

print(divide_num)


# Square numbers using lambda and map()
numbers = [2, 3, 4, 5]

square_num = list(map(lambda num: num * num, numbers))

print(square_num)


# Apply a 20% discount to each price
prices = [100, 200, 300, 400]

new_list_price = list(map(lambda price: price * 0.80, prices))

print(new_list_price)