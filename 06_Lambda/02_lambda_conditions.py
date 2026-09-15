# Q6: Check whether a number is even
is_even = lambda num: True if num % 2 == 0 else False
print("Is Even:", is_even(8))


# Q7: Check whether a number is positive, negative, or zero
check_number = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print("Number 9:", check_number(9))
print("Number -4:", check_number(-4))
print("Number 0:", check_number(0))


# Q8: Categorize a person based on age
check_age = lambda age: "Child" if age <= 12 else "Teenager" if age >= 13 and age <= 19 else "Adult"
print("Age 9:", check_age(9))
print("Age 17:", check_age(17))
print("Age 25:", check_age(25))


# Q9: Calculate discount based on price
get_discount = lambda amount: "20% Discount" if amount >= 1000 else "10% Discount" if amount >= 500 and amount <= 999 else "No Discount"
print("Amount 1100:", get_discount(1100))
print("Amount 700:", get_discount(700))
print("Amount 300:", get_discount(300))


# Q10: Identify which number is larger
max_num = lambda num1, num2: num1 if num1 > num2 else num2
print("Larger number:", max_num(3, 6))
print("Larger number:", max_num(6, 3))