# Store expense information
expenses = [
    {"name": "Hotel", "amount": 2400},
    {"name": "Food", "amount": 1200},
    {"name": "Travel", "amount": 900},
    {"name": "Tickets", "amount": 1500}
]

people = 3

# Calculate each person's share
expense_records = list(
    map(
        lambda expense: {
            **expense,
            "share": round(expense["amount"] / people, 2)
        },
        expenses
    )
)

# Find expenses above ₹1000
large_expenses = list(
    filter(
        lambda expense: expense["amount"] > 1000,
        expense_records
    )
)

# Calculate total expense
total_expense = sum(
    expense["amount"] for expense in expense_records
)

# Calculate total share per person
share_per_person = round(
    total_expense / people,
    2
)

# Display results
print("\n" + "=" * 50)
print("          💰 EXPENSE SPLITTER")
print("=" * 50)

print("\n📋 EXPENSES")
print("-" * 50)

for expense in expense_records:
    print(
        f"{expense['name']:<15} "
        f"₹{expense['amount']:<8} "
        f"Share: ₹{expense['share']}"
    )

print("\n🔎 LARGE EXPENSES")
print("-" * 50)

for expense in large_expenses:
    print(
        f"{expense['name']:<15} "
        f"₹{expense['amount']}"
    )

print("\n📊 SUMMARY")
print("-" * 50)
print(f"People                : {people}")
print(f"Total expense         : ₹{total_expense}")
print(f"Share per person      : ₹{share_per_person}")
print(f"Large expenses        : {len(large_expenses)}")
print("=" * 50)