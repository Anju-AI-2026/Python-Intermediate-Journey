
students = [
    {"name": "Asha", "present": True},
    {"name": "Meera", "present": False},
    {"name": "Anji", "present": True},
    {"name": "Priya", "present": True},
    {"name": "Sneha", "present": False},
]

print("=" * 45)
print("       STUDENT ATTENDANCE REPORT")
print("=" * 45)

present_count = 0
absent_count = 0

for roll_no, student in enumerate(students, start=1):
    status = "Present" if student["present"] else "Absent"

    if student["present"]:
        present_count += 1
    else:
        absent_count += 1

    print(
        f"{roll_no}. {student['name']:<12} | {status}"
    )

print("-" * 45)
print(f"Total students : {len(students)}")
print(f"Present        : {present_count}")
print(f"Absent         : {absent_count}")
print(
    f"Attendance     : {present_count / len(students) * 100:.1f}%"
)
print("=" * 45)
