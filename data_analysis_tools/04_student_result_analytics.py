
# Student Result Analytics
# Analyzes marks, grades, class averages, and top performers


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def analyze_results(students, passing_mark=40):
    if not students:
        raise ValueError("At least one student is required.")

    results = []

    for student in students:
        marks = student["marks"]

        if not marks:
            raise ValueError(
                f"No marks provided for {student['name']}."
            )

        if any(not 0 <= mark <= 100 for mark in marks):
            raise ValueError(
                f"Invalid marks found for {student['name']}."
            )

        average = sum(marks) / len(marks)
        results.append({
            "name": student["name"],
            "average": average,
            "grade": calculate_grade(average),
            "status": "PASS" if average >= passing_mark else "FAIL",
        })

    return sorted(
        results,
        key=lambda result: result["average"],
        reverse=True,
    )


students = [
    {"name": "Asha", "marks": [92, 88, 95, 90]},
    {"name": "Meera", "marks": [78, 82, 85, 80]},
    {"name": "Rahul", "marks": [35, 42, 38, 45]},
    {"name": "Priya", "marks": [88, 91, 86, 94]},
    {"name": "Sneha", "marks": [65, 72, 68, 70]},
    {"name": "Kavya", "marks": [55, 48, 62, 58]},
]

results = analyze_results(students)

grade_distribution = {}

for result in results:
    grade = result["grade"]
    grade_distribution[grade] = grade_distribution.get(grade, 0) + 1

class_average = sum(
    result["average"] for result in results
) / len(results)

passed = sum(result["status"] == "PASS" for result in results)
failed = len(results) - passed

print("=" * 70)
print("                    STUDENT RESULT ANALYTICS")
print("=" * 70)

print(
    f"{'Rank':<6} {'Student':<12} "
    f"{'Average':>10} {'Grade':>8} {'Status':>10}"
)
print("-" * 70)

for rank, result in enumerate(results, start=1):
    print(
        f"{rank:<6} {result['name']:<12} "
        f"{result['average']:>9.2f} "
        f"{result['grade']:>8} "
        f"{result['status']:>10}"
    )

print("-" * 70)
print(f"Class average: {class_average:.2f}")
print(f"Students passed: {passed}")
print(f"Students failed: {failed}")

print("\nGRADE DISTRIBUTION")

for grade in ("A+", "A", "B", "C", "D", "F"):
    print(f"Grade {grade}: {grade_distribution.get(grade, 0)} student(s)")

print("-" * 70)
print(f"Class topper: {results[0]['name']} ({results[0]['average']:.2f})")
print("=" * 70)
