# Store inventory information
products = [
    {"name": "Laptop", "stock": 8, "minimum": 5},
    {"name": "Mouse", "stock": 3, "minimum": 10},
    {"name": "Keyboard", "stock": 12, "minimum": 8},
    {"name": "Monitor", "stock": 4, "minimum": 6},
    {"name": "Webcam", "stock": 15, "minimum": 10}
]

# Generate stock status
inventory = list(
    map(
        lambda product: {
            **product,
            "status": (
                "REORDER" 
                if product["stock"] < product["minimum"]
                else "SUFFICIENT"
            )
        },
        products
    )
)

# Find products requiring reorder
reorder_products = list(
    filter(
        lambda product: product["status"] == "REORDER",
        inventory
    )
)

# Calculate required quantity
reorder_details = list(
    map(
        lambda product: {
            "name": product["name"],
            "required": product["minimum"] - product["stock"]
        },
        reorder_products
    )
)

# Calculate total units currently available
total_stock = sum(
    product["stock"] for product in inventory
)

# Display inventory
print("\n" + "=" * 55)
print("          📦 INVENTORY ALERT SYSTEM")
print("=" * 55)

print("\n📋 INVENTORY STATUS")
print("-" * 55)

for product in inventory:
    print(
        f"{product['name']:<15} "
        f"Stock: {product['stock']:<4} "
        f"Minimum: {product['minimum']:<4} "
        f"{product['status']}"
    )

print("\n⚠️ REORDER REQUIRED")
print("-" * 55)

for product in reorder_details:
    print(
        f"{product['name']:<15} "
        f"Additional units: {product['required']}"
    )

print("\n📊 INVENTORY SUMMARY")
print("-" * 55)
print(f"Product types       : {len(inventory)}")
print(f"Total units         : {total_stock}")
print(f"Reorder alerts      : {len(reorder_products)}")
print("=" * 55)