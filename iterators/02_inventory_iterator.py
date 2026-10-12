
# Inventory Iterator and Stock Alert System

products = [
    {"name": "Keyboard", "stock": 12},
    {"name": "Mouse", "stock": 3},
    {"name": "Monitor", "stock": 8},
    {"name": "USB Cable", "stock": 0},
    {"name": "Headphones", "stock": 4},
]

product_iterator = iter(products)
minimum_stock = 5

low_stock = []
processed = 0

print("=" * 40)
print("       INVENTORY STOCK AUDIT")
print("=" * 40)

while True:
    try:
        product = next(product_iterator)
        processed += 1

        if product["stock"] < minimum_stock:
            low_stock.append(product)

            print(
                f"ALERT: {product['name']} "
                f"has only {product['stock']} units."
            )

    except StopIteration:
        break

print("-" * 40)
print("Products processed:", processed)
print("Products requiring attention:", len(low_stock))
print("=" * 40)
