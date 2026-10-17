
# Student Performance Stream
# Generates student records and analyzes results incrementally


def student_stream(students):

    for student in students:
        yield student


students = [
    {"name": "Asha", "score": 82},
    {"name": "Meera", "score": 36},
    {"name": "Anji", "score": 95},
    {"name": "Priya", "score": 67},
    {"name": "Sneha", "score": 28},
    {"name": "Kavya", "score": 89},
]

passing_score = 40
total_score = 0
passed = 0
failed = 0
top_student = None
processed = 0

print("=" * 50)
print("       STUDENT PERFORMANCE STREAM")
print("=" * 50)

for position, student in enumerate(student_stream(students), start=1):

    score = student["score"]
    status = "PASS" if score >= passing_score else "FAIL"

    total_score += score
    processed += 1

    if score >= passing_score:
        passed += 1
    else:
        failed += 1

    if top_student is None or score > top_student["score"]:
        top_student = student

    print(
        f"{position}. {student['name']:<10} "
        f"| Score: {score:>3} | {status}"
    )

print("-" * 50)
print("Students processed:", processed)
print("Passed:", passed)
print("Failed:", failed)
print(f"Class average: {total_score / processed:.2f}")
print(
    f"Top performer: {top_student['name']} "
    f"({top_student['score']})"
)
print("=" * 50)
