# Store student marks
students = [
    {"name": "Aarav", "marks": 92},
    {"name": "Meera", "marks": 87},
    {"name": "Rohan", "marks": 95},
    {"name": "Diya", "marks": 78},
    {"name": "Kabir", "marks": 84}
]

# Sort students by marks
ranked_students = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

# Add rank information
ranked_students = [
    {
        **student,
        "rank": index + 1
    }
    for index, student in enumerate(ranked_students)
]

# Find students scoring 85 or above
high_scorers = list(
    filter(
        lambda student: student["marks"] >= 85,
        ranked_students
    )
)

# Calculate average marks
average_marks = round(
    sum(student["marks"] for student in ranked_students)
    / len(ranked_students),
    2
)

# Display ranking
print("\n" + "=" * 50)
print("           🏆 STUDENT RANK MANAGER")
print("=" * 50)

print("\n📋 RANKING")
print("-" * 50)

for student in ranked_students:
    print(
        f"Rank {student['rank']:<3} "
        f"{student['name']:<15} "
        f"{student['marks']} marks"
    )

print("\n🌟 HIGH SCORERS")
print("-" * 50)

for student in high_scorers:
    print(
        f"{student['name']:<15} "
        f"{student['marks']} marks"
    )

print("\n📊 CLASS SUMMARY")
print("-" * 50)
print(f"Total students      : {len(ranked_students)}")
print(f"High scorers        : {len(high_scorers)}")
print(f"Class average       : {average_marks}")
print(f"Top student         : {ranked_students[0]['name']}")
print(f"Top marks           : {ranked_students[0]['marks']}")
print("=" * 50)