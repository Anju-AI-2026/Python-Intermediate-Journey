# Store student quiz scores
students = [
    {"name": "Aarav", "score": 88, "total": 100},
    {"name": "Meera", "score": 72, "total": 100},
    {"name": "Rohan", "score": 95, "total": 100},
    {"name": "Diya", "score": 61, "total": 100},
    {"name": "Kabir", "score": 80, "total": 100}
]


# Calculate percentage and grade
def assign_grade(percentage):

    if percentage >= 90:
        return "A"

    elif percentage >= 80:
        return "B"

    elif percentage >= 70:
        return "C"

    elif percentage >= 60:
        return "D"

    else:
        return "F"


# Transform student records
results = list(
    map(
        lambda student: {
            **student,
            "percentage": round(
                student["score"] / student["total"] * 100, 2
            ),
            "grade": assign_grade(
                student["score"] / student["total"] * 100
            )
        },
        students
    )
)


# Find students scoring 80% or above
high_performers = list(
    filter(
        lambda student: student["percentage"] >= 80,
        results
    )
)


# Calculate class average
average_score = round(
    sum(student["percentage"] for student in results)
    / len(results),
    2
)


# Find the highest scorer
top_student = max(
    results,
    key=lambda student: student["percentage"]
)


# Display results
print("\n" + "=" * 55)
print("           🏆 QUIZ SCORE MANAGER")
print("=" * 55)

print("\n📋 STUDENT RESULTS")
print("-" * 55)

for student in results:
    print(
        f"{student['name']:<15} "
        f"{student['score']}/{student['total']} "
        f"{student['percentage']}% "
        f"Grade: {student['grade']}"
    )


print("\n🌟 HIGH PERFORMERS")
print("-" * 55)

for student in high_performers:
    print(
        f"{student['name']:<15} "
        f"{student['percentage']}%"
    )


print("\n📊 CLASS SUMMARY")
print("-" * 55)
print(f"Total students     : {len(results)}")
print(f"High performers    : {len(high_performers)}")
print(f"Class average      : {average_score}%")
print(f"Top student        : {top_student['name']}")
print(f"Highest percentage : {top_student['percentage']}%")
print(f"Highest grade      : {top_student['grade']}")
print("=" * 55)