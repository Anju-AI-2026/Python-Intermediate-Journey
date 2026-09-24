# 1
names = ["Anju", "Ravi", "Rossy", "Arjun"]
marks = [85, 72, 91, 76]

mark_name = list(zip(names, marks))
print(mark_name)


# 2
subjects = ["Python", "DBMS", "Networking", "Math"]
scores = [92, 85, 78, 95]

for subject, score in zip(subjects, scores):
    print(f"{subject} ➡️   {score}")


# 3
names = ["Anju", "Ravi", "Rossy", "Arjun"]
ages = [18, 19, 18]

name_age = list(zip(names, ages))
print(name_age)


# 4
students = ["Anju", "Ravi", "Rossy", "Arjun"]
scores = [85, 72, 91, 76]

student_score = dict(zip(students, scores))
print(student_score)


# 5
names = ["Anju", "Ravi", "Rossy", "Arjun"]
marks = [85, 72, 91, 76]
grades = ["A", "B", "A+", "B+"]

for name, mark, grade in zip(names, marks, grades):
    print(f"{name}  ➡️    {mark}  ➡️   {grade}")