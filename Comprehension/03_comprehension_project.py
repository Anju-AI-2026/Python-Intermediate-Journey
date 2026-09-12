# Program 1: Find the length of each word using list comprehension
words = ["python", "AI", "programming", "code", "computer"]
len_words = [len(word) for word in words ]
print(len_words)


# Program 2: Create a list containing words whose length is greater than 5
words = ["python", "AI", "programming", "code", "computer", "ML"]
big_word = [word for word in words if len(word) > 5]
print(big_word)


# Program 3: Create a list of cubes from numbers in a tuple
numbers = (2, 3, 4, 5, 6)
cube_num = [num*num*num for num in numbers]
print(cube_num)


# Program 4: Create a set of squares from numbers in a set
numbers = {2, 3, 4, 5, 6}
square_num = {num*num for num in numbers}
print(square_num)