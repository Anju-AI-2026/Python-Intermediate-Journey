# 11
names = ["Anju", "Ravi", "Rossy", "Arjun"]
marks = [85, 72, 91, 76]

new_dict = {name: mark for name, mark in zip(names, marks)}

print(new_dict)


# 12
names = ["Anju", "Ravi", "Rossy", "Arjun"]
marks = [85, 72, 91, 64]

name_marks = {
    name: mark
    for name, mark in zip(names, marks)
    if mark >= 75
}

print(name_marks)


# 13
names = ["Anju", "Ravi", "Rossy", "Arjun"]
marks = [85, 72, 91, 64]
subjects = ["Python", "DBMS", "Python", "Networking"]

highest_mark = 0
highest_name = ""

for name, mark, subject in zip(names, marks, subjects):

    if subject == "Python" and mark > highest_mark:
        highest_mark = mark
        highest_name = name

print(f"{highest_name} → {highest_mark}")


# 14
names = ["Anju", "Ravi", "Rossy", "Arjun"]
python_marks = [85, 72, 91, 64]
dbms_marks = [78, 88, 95, 70]

zipped_data = list(zip(python_marks, dbms_marks))

new_pd = list(
    map(
        lambda pd_element: pd_element[0] + pd_element[1],
        zipped_data
    )
)

print(new_pd)


# 15
names = ["Anju", "Ravi", "Rossy", "Arjun"]

python_marks = [85, 72, 91, 64]

dbms_marks = [78, 88, 95, 70]


# Combine the related data
zipped_data = list(zip(names, python_marks, dbms_marks))


# Keep students who scored at least 75 in both subjects
filtered_data = list(
    filter(
        lambda student: student[1] >= 75 and student[2] >= 75,
        zipped_data
    )
)

print(filtered_data)