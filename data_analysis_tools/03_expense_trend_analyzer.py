
# Expense Trend Analyzer
# Analyzes spending patterns, monthly totals, and budget limits

from collections import defaultdict


def analyze_expenses(expenses, monthly_budget):
    if monthly_budget <= 0:
        raise ValueError("Monthly budget must be greater than zero.")

    category_totals = defaultdict(float)
    monthly_totals = defaultdict(float)

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]
        month = expense["month"]

        if amount < 0:
            raise ValueError("Expense amounts cannot be negative.")

        category_totals[category] += amount
        monthly_totals[month] += amount

    ranked_categories = sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    ranked_months = sorted(monthly_totals.items())

    return ranked_categories, ranked_months


expenses = [
    {"month": "January", "category": "Food", "amount": 4500},
    {"month": "January", "category": "Travel", "amount": 1800},
    {"month": "January", "category": "Education", "amount": 2500},
    {"month": "February", "category": "Food", "amount": 5200},
    {"month": "February", "category": "Travel", "amount": 2400},
    {"month": "February", "category": "Shopping", "amount": 1900},
    {"month": "March", "category": "Food", "amount": 4800},
    {"month": "March", "category": "Education", "amount": 3200},
    {"month": "March", "category": "Shopping", "amount": 2100},
]

monthly_budget = 10000

category_totals, monthly_totals = analyze_expenses(
    expenses,
    monthly_budget,
)

print("=" * 65)
print("                   EXPENSE TREND ANALYZER")
print("=" * 65)

print("\nSPENDING BY CATEGORY")
print("-" * 45)

for category, total in category_totals:
    print(f"{category:<18} | ₹{total:>10,.2f}")

if category_totals:
    print(
        f"\nHighest spending category: "
        f"{category_totals[0][0]}"
    )

print("\nMONTHLY SPENDING")
print("-" * 65)
print(f"{'Month':<15} {'Total Expenses':>18} {'Budget Status':>20}")
print("-" * 65)

for month, total in monthly_totals:
    status = "OVER BUDGET" if total > monthly_budget else "Within budget"
    print(f"{month:<15} ₹{total:>17,.2f} {status:>20}")

print("-" * 65)

overall_total = sum(total for _, total in monthly_totals)
print(f"Total expenses across all months: ₹{overall_total:,.2f}")

if monthly_totals:
    average_monthly = overall_total / len(monthly_totals)
    print(f"Average monthly expenses:          ₹{average_monthly:,.2f}")

print("=" * 65)
