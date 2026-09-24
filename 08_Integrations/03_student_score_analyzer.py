# Store all student data
students = []


# Get student details
def add_students(students):

    student_num = int(input("How many students do you want to enter? : "))

    for _ in range(student_num):

        name = input("Student name : ")
        marks = int(input("Marks : "))

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)


# Add students
add_students(students)


# Calculate percentages using map()
percentages = list(
    map(
        lambda student: {
            "name": student["name"],
            "percentage": student["marks"]
        },
        students
    )
)


# Find students scoring 80% or above
high_scorers = list(
    filter(
        lambda student: student["percentage"] >= 80,
        percentages
    )
)


# Find highest percentage
highest_percentage = max(
    percentages,
    key=lambda student: student["percentage"]
)


# Display results
print("\n" + "=" * 40)
print("       📊 STUDENT SCORE ANALYZER")
print("=" * 40)

print("\n📋 ALL STUDENTS")
print("-" * 40)

for student in percentages:
    print(f"{student['name']:<20} → {student['percentage']}%")


print("\n🏆 STUDENTS ABOVE 80%")
print("-" * 40)

for student in high_scorers:
    print(f"{student['name']:<20} → {student['percentage']}%")


print("\n📊 SUMMARY")
print("-" * 40)
print(f"Total Students      : {len(students)}")
print(f"Students Above 80%  : {len(high_scorers)}")
print(f"Highest Percentage  : {highest_percentage['percentage']}%")
print(f"Top Student         : {highest_percentage['name']}")

print("=" * 40)