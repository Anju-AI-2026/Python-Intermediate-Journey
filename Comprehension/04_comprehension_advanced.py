# Program 5: Create a list containing only the student names from a dictionary
students = {
    "Anjali": 92,
    "Riya": 78,
    "Sara": 85,
    "Meena": 69
}
names = [name for name in students.keys()]
print(names)


# Program 6: Create a list containing marks greater than 75
students = {
    "Anjali": 92,
    "Riya": 78,
    "Sara": 85,
    "Meena": 69
}
marks = [mark for mark in students.values() if mark > 75]
print(marks)


# Program 7: Create a dictionary with each word as the key and its length as the value
words = ["apple", "cat", "elephant", "dog"]
new_dict = {word : len(word) for word in words}
print(new_dict)


# Program 8: Create a list containing contact names whose length is greater than 5
contacts = ["Anjali", "Riya", "Sakshi", "Meena", "Priyanka"]
new_contacts = [name for name in contacts if len(name) > 5]
print(new_contacts)