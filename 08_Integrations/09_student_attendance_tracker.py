# Store student attendance information
students = [
    {"name": "Anjali", "present": 22, "total": 25},
    {"name": "Ravi", "present": 18, "total": 25},
    {"name": "Priya", "present": 24, "total": 25},
    {"name": "Arjun", "present": 15, "total": 25},
    {"name": "Sneha", "present": 20, "total": 25},
    {"name": "Kiran", "present": 23, "total": 25}
]


# Calculate attendance percentage
attendance_records = list(
    map(
        lambda student: {
            **student,
            "percentage": round(
                student["present"] / student["total"] * 100, 2
            )
        },
        students
    )
)


# Identify students below 75% attendance
low_attendance = list(
    filter(
        lambda student: student["percentage"] < 75,
        attendance_records
    )
)


# Identify students with at least 90% attendance
high_attendance = list(
    filter(
        lambda student: student["percentage"] >= 90,
        attendance_records
    )
)


# Calculate class attendance percentage
total_present = sum(
    student["present"] for student in attendance_records
)

total_classes = sum(
    student["total"] for student in attendance_records
)

class_percentage = round(
    total_present / total_classes * 100, 2
)


# Find the student with the highest attendance
top_attendance = max(
    attendance_records,
    key=lambda student: student["percentage"]
)


# Display attendance records
print("\n" + "=" * 60)
print("           📅 STUDENT ATTENDANCE TRACKER")
print("=" * 60)

print("\n📋 ALL STUDENTS")
print("-" * 60)

for student in attendance_records:
    print(
        f"{student['name']:<15} "
        f"{student['present']}/{student['total']} classes "
        f"→ {student['percentage']}%"
    )


print("\n⚠️ STUDENTS BELOW 75%")
print("-" * 60)

for student in low_attendance:
    print(
        f"{student['name']:<15} "
        f"{student['percentage']}%"
    )


print("\n🏆 STUDENTS WITH AT LEAST 90%")
print("-" * 60)

for student in high_attendance:
    print(
        f"{student['name']:<15} "
        f"{student['percentage']}%"
    )


# Display summary
print("\n📊 ATTENDANCE SUMMARY")
print("-" * 60)
print(f"Total students          : {len(attendance_records)}")
print(f"Students below 75%      : {len(low_attendance)}")
print(f"Students at least 90%   : {len(high_attendance)}")
print(f"Class attendance        : {class_percentage}%")
print(f"Highest attendance      : {top_attendance['name']}")
print(f"Top attendance          : {top_attendance['percentage']}%")
print("=" * 60)