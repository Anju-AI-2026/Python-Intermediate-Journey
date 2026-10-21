
# Employee Attendance Analyzer
# Calculates attendance rates and identifies low attendance

def analyze_attendance(employees, total_working_days, minimum_rate=75):
    if total_working_days <= 0:
        raise ValueError("Working days must be greater than zero.")

    if not 0 <= minimum_rate <= 100:
        raise ValueError("Minimum attendance must be between 0 and 100.")

    results = []

    for employee in employees:
        name = employee["name"]
        present_days = employee["present_days"]

        if not 0 <= present_days <= total_working_days:
            raise ValueError(
                f"Invalid attendance count for {name}."
            )

        absent_days = total_working_days - present_days
        attendance_rate = present_days / total_working_days * 100

        results.append({
            "name": name,
            "present": present_days,
            "absent": absent_days,
            "percentage": attendance_rate,
            "eligible": attendance_rate >= minimum_rate,
        })

    return sorted(
        results,
        key=lambda item: item["percentage"],
        reverse=True,
    )


employees = [
    {"name": "Asha", "present_days": 22},
    {"name": "Meera", "present_days": 18},
    {"name": "Rahul", "present_days": 14},
    {"name": "Priya", "present_days": 20},
    {"name": "Sneha", "present_days": 24},
    {"name": "Kavya", "present_days": 16},
]

total_working_days = 24
minimum_rate = 75

results = analyze_attendance(
    employees,
    total_working_days,
    minimum_rate,
)

print("=" * 75)
print("                     EMPLOYEE ATTENDANCE ANALYZER")
print("=" * 75)
print(f"Working days: {total_working_days}")
print(f"Minimum attendance requirement: {minimum_rate}%")

print("-" * 75)
print(
    f"{'Employee':<12} {'Present':>8} {'Absent':>8} "
    f"{'Attendance':>12} {'Status':>12}"
)
print("-" * 75)

for result in results:
    status = "ELIGIBLE" if result["eligible"] else "LOW ATTENDANCE"

    print(
        f"{result['name']:<12} "
        f"{result['present']:>8} "
        f"{result['absent']:>8} "
        f"{result['percentage']:>11.2f}% "
        f"{status:>12}"
    )

eligible_count = sum(result["eligible"] for result in results)
low_count = len(results) - eligible_count

print("-" * 75)
print("Employees analyzed:", len(results))
print("Meeting attendance requirement:", eligible_count)
print("Below attendance requirement:", low_count)
print("=" * 75)
