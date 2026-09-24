# Store all expenses
expenses = []


# Get expense details
def add_expenses(expenses):

    expense_num = int(input("How many expenses do you want to enter? : "))

    for _ in range(expense_num):

        name = input("Expense name : ")
        category = input("Category : ")
        amount = int(input("Amount : "))

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)


# Add expenses
add_expenses(expenses)


# Find food expenses
food_expenses = list(
    filter(
        lambda expense: expense["category"].lower() == "food",
        expenses
    )
)


# Find expenses above ₹500
high_expenses = list(
    filter(
        lambda expense: expense["amount"] > 500,
        expenses
    )
)


# Extract all expense amounts using map()
amounts = list(
    map(
        lambda expense: expense["amount"],
        expenses
    )
)


# Calculate total expense
total_expense = sum(amounts)


# Display results
print("\n" + "=" * 45)
print("        💰 EXPENSE CATEGORY ANALYZER")
print("=" * 45)

print("\n📋 ALL EXPENSES")
print("-" * 45)

for expense in expenses:
    print(
        f"{expense['name']:<15} "
        f"{expense['category']:<12} "
        f"₹{expense['amount']}"
    )


print("\n🍔 FOOD EXPENSES")
print("-" * 45)

for expense in food_expenses:
    print(
        f"{expense['name']:<15} "
        f"₹{expense['amount']}"
    )


print("\n🔎 EXPENSES ABOVE ₹500")
print("-" * 45)

for expense in high_expenses:
    print(
        f"{expense['name']:<15} "
        f"{expense['category']:<12} "
        f"₹{expense['amount']}"
    )


print("\n📊 SUMMARY")
print("-" * 45)
print(f"Total expenses       : {len(expenses)}")
print(f"Expenses above ₹500  : {len(high_expenses)}")
print(f"Total amount         : ₹{total_expense}")
print("=" * 45)