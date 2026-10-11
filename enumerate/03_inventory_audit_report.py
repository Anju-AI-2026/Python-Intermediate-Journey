
products = [
    {"name": "Keyboard", "stock": 12, "minimum": 5},
    {"name": "Mouse", "stock": 3, "minimum": 5},
    {"name": "Monitor", "stock": 8, "minimum": 4},
    {"name": "USB Cable", "stock": 0, "minimum": 10},
    {"name": "Headphones", "stock": 4, "minimum": 4},
]

low_stock = 0
out_of_stock = 0

print("=" * 60)
print("                  INVENTORY AUDIT REPORT")
print("=" * 60)

for item_no, product in enumerate(products, start=1):
    stock = product["stock"]
    minimum = product["minimum"]

    if stock == 0:
        status = "OUT OF STOCK"
        out_of_stock += 1
    elif stock <= minimum:
        status = "REORDER"
        low_stock += 1
    else:
        status = "AVAILABLE"

    print(
        f"{item_no}. {product['name']:<14} "
        f"| Stock: {stock:>3} "
        f"| Minimum: {minimum:>3} "
        f"| {status}"
    )

print("-" * 60)
print(f"Products audited : {len(products)}")
print(f"Low-stock items  : {low_stock}")
print(f"Out-of-stock     : {out_of_stock}")
print("=" * 60)
