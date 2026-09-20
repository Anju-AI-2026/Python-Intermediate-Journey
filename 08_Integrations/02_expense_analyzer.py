
# Store all expenses
expenses = []


# Get expense details from the user
def expenses_analyse(expenses):

    while True:
        expense_num = input("How many expenses do you want to enter ?")

        if expense_num.isalpha():
            print("Please enter a valid number")
            break

        expense_num = int(expense_num)

        for _ in range(0, expense_num):

            while True:
                expense_name = input("Expense name :")

                if expense_name.isnumeric():
                    print("Expense name should not be a number")
                else:
                    break

            while True:
                expense_amount = input("Amount :")

                if expense_amount.isalpha():
                    print("Expense name should be a number")
                else:
                    expense_amount = int(expense_amount)

                    expense_dict = {
                        "expense_name": expense_name,
                        "expense_amount": expense_amount
                    }

                    expenses.append(expense_dict)
                    break

        return


# Collect expenses
expenses_analyse(expenses)


# Display all expenses
print("\n" + "=" * 40)
print("        💰 EXPENSE ANALYZER")
print("=" * 40)

print("\n📋 ALL EXPENSES")
print("-" * 40)

for expense in expenses:
    print(f"{expense['expense_name']:<20} ₹{expense['expense_amount']}")


# Filter expenses above ₹500
filtered_expense = list(
    filter(
        lambda expense: expense["expense_amount"] > 500,
        expenses
    )
)


# Display filtered expenses
print("\n🔎 EXPENSES ABOVE ₹500")
print("-" * 40)

for item in filtered_expense:
    print(f"{item['expense_name']:<20} ₹{item['expense_amount']}")


# Calculate total of all expenses
def total_amount(expenses):

    total = 0

    for item in expenses:
        total = total + int(item["expense_amount"])

    return total


total_expense = total_amount(expenses)


# Display summary
print("\n📊 SUMMARY")
print("-" * 40)
print(f"Expenses above ₹500 : {len(filtered_expense)}")
print(f"Total expenses       : ₹{total_expense}")
print("=" * 40)

        
