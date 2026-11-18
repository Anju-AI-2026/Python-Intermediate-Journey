# Store the numbers to check
numbers = [1, 2, 3, 4]

# Store numbers that have already been seen
new_num = []


# Check whether a duplicate number exists
def seen_num():

    for num in numbers:

        if num in new_num:
            return True

        else:
            new_num.append(num)

    return False


# Display whether a duplicate was found
if seen_num() == True:

    print("True")

else:

    print("False")