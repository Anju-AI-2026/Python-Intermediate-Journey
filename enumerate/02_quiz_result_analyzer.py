
students = [
    {"name": "Asha", "score": 82},
    {"name": "Meera", "score": 46},
    {"name": "Anji", "score": 95},
    {"name": "Priya", "score": 67},
    {"name": "Sneha", "score": 31},
]

passing_score = 40
passed = 0
failed = 0
total_score = 0

print("=" * 45)
print("          QUIZ RESULT ANALYZER")
print("=" * 45)

for position, student in enumerate(students, start=1):
    score = student["score"]
    result = "PASS" if score >= passing_score else "FAIL"

    total_score += score

    if score >= passing_score:
        passed += 1
    else:
        failed += 1

    print(
        f"{position}. {student['name']:<10} "
        f"| Score: {score:>3} | {result}"
    )

average = total_score / len(students)

top_student = max(students, key=lambda student: student["score"])

print("-" * 45)
print(f"Students passed : {passed}")
print(f"Students failed : {failed}")
print(f"Class average   : {average:.2f}")
print(
    f"Top performer   : {top_student['name']} "
    f"({top_student['score']})"
)
print("=" * 45)
