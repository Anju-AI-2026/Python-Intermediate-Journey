# Store employee information
employee_names = [
    "Anjali",
    "Ravi",
    "Priya",
    "Arjun",
    "Sneha"
]

basic_salaries = [
    30000,
    25000,
    40000,
    35000,
    28000
]

allowances = [
    5000,
    3000,
    6000,
    4000,
    3500
]


# Combine employee data using zip()
employees = list(
    map(
        lambda data: {
            "name": data[0],
            "basic_salary": data[1],
            "allowance": data[2]
        },
        zip(employee_names, basic_salaries, allowances)
    )
)


# Calculate total salary for each employee
payroll = list(
    map(
        lambda employee: {
            **employee,
            "total_salary": (
                employee["basic_salary"] + employee["allowance"]
            )
        },
        employees
    )
)


# Find employees earning above ₹35,000
high_salary_employees = list(
    filter(
        lambda employee: employee["total_salary"] > 35000,
        payroll
    )
)


# Calculate total payroll amount
total_payroll = sum(
    employee["total_salary"]
    for employee in payroll
)


# Find the highest-paid employee
highest_paid = max(
    payroll,
    key=lambda employee: employee["total_salary"]
)


# Display payroll
print("\n" + "=" * 55)
print("           💼 EMPLOYEE PAYROLL ANALYZER")
print("=" * 55)

print("\n📋 EMPLOYEE PAYROLL")
print("-" * 55)

for employee in payroll:
    print(
        f"{employee['name']:<15} "
        f"Basic: ₹{employee['basic_salary']:<8} "
        f"Allowance: ₹{employee['allowance']:<6} "
        f"Total: ₹{employee['total_salary']}"
    )


print("\n💰 EMPLOYEES ABOVE ₹35,000")
print("-" * 55)

for employee in high_salary_employees:
    print(
        f"{employee['name']:<15} "
        f"Total Salary: ₹{employee['total_salary']}"
    )


print("\n📊 PAYROLL SUMMARY")
print("-" * 55)
print(f"Total employees       : {len(payroll)}")
print(f"Employees above limit : {len(high_salary_employees)}")
print(f"Total payroll         : ₹{total_payroll}")
print(f"Highest-paid employee : {highest_paid['name']}")
print(f"Highest salary        : ₹{highest_paid['total_salary']}")
print("=" * 55)