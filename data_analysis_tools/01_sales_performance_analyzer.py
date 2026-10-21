
# Sales Performance Analyzer
# Analyzes revenue, units sold, and product performance

from collections import defaultdict


def analyze_sales(sales_records):
    revenue_by_product = defaultdict(float)
    units_by_product = defaultdict(int)
    total_revenue = 0.0
    total_units = 0

    for record in sales_records:
        product = record["product"]
        quantity = record["quantity"]
        price = record["unit_price"]

        revenue = quantity * price

        revenue_by_product[product] += revenue
        units_by_product[product] += quantity
        total_revenue += revenue
        total_units += quantity

    ranked_products = sorted(
        revenue_by_product.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return total_revenue, total_units, ranked_products, units_by_product


sales_records = [
    {"product": "Laptop", "quantity": 4, "unit_price": 45000},
    {"product": "Mouse", "quantity": 20, "unit_price": 500},
    {"product": "Keyboard", "quantity": 10, "unit_price": 1200},
    {"product": "Monitor", "quantity": 6, "unit_price": 12000},
    {"product": "Laptop", "quantity": 2, "unit_price": 45000},
    {"product": "Mouse", "quantity": 15, "unit_price": 500},
    {"product": "Monitor", "quantity": 3, "unit_price": 12000},
]

total_revenue, total_units, ranked_products, units_by_product = (
    analyze_sales(sales_records)
)

print("=" * 65)
print("                  SALES PERFORMANCE ANALYZER")
print("=" * 65)

print(f"Total revenue:       ₹{total_revenue:,.2f}")
print(f"Total units sold:    {total_units}")
print(f"Unique products:     {len(units_by_product)}")

print("-" * 65)
print(f"{'Product':<15} {'Units Sold':>12} {'Revenue':>20}")
print("-" * 65)

for product, revenue in ranked_products:
    print(
        f"{product:<15} "
        f"{units_by_product[product]:>12} "
        f"₹{revenue:>19,.2f}"
    )

print("-" * 65)

if ranked_products:
    top_product, top_revenue = ranked_products[0]
    print(f"Top product by revenue: {top_product}")
    print(f"Product revenue:        ₹{top_revenue:,.2f}")

print("=" * 65)
