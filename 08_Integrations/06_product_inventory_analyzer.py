# Store product information
product_names = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones",
    "Webcam"
]

product_prices = [
    55000,
    800,
    1500,
    12000,
    2500,
    1800
]

product_stock = [
    5,
    25,
    12,
    8,
    15,
    20
]


# Combine product data using zip()
products = list(
    map(
        lambda data: {
            "name": data[0],
            "price": data[1],
            "stock": data[2]
        },
        zip(product_names, product_prices, product_stock)
    )
)


# Calculate inventory value for each product
inventory = list(
    map(
        lambda product: {
            "name": product["name"],
            "price": product["price"],
            "stock": product["stock"],
            "value": product["price"] * product["stock"]
        },
        products
    )
)


# Find products with stock greater than 10
high_stock_products = list(
    filter(
        lambda product: product["stock"] > 10,
        inventory
    )
)


# Find products worth more than ₹20,000 in inventory
high_value_products = list(
    filter(
        lambda product: product["value"] > 20000,
        inventory
    )
)


# Calculate total inventory value
total_inventory_value = sum(
    product["value"]
    for product in inventory
)


# Calculate total number of products in stock
total_stock = sum(
    product["stock"]
    for product in inventory
)


# Find the most valuable inventory item
most_valuable = max(
    inventory,
    key=lambda product: product["value"]
)


# Display inventory
print("\n" + "=" * 55)
print("           📦 PRODUCT INVENTORY ANALYZER")
print("=" * 55)

print("\n📋 PRODUCT INVENTORY")
print("-" * 55)

for product in inventory:
    print(
        f"{product['name']:<15} "
        f"₹{product['price']:<8} "
        f"Stock: {product['stock']:<3} "
        f"Value: ₹{product['value']}"
    )


print("\n📈 HIGH STOCK PRODUCTS")
print("-" * 55)

for product in high_stock_products:
    print(
        f"{product['name']:<15} "
        f"Stock: {product['stock']}"
    )


print("\n💰 HIGH VALUE INVENTORY")
print("-" * 55)

for product in high_value_products:
    print(
        f"{product['name']:<15} "
        f"Inventory Value: ₹{product['value']}"
    )


print("\n📊 SUMMARY")
print("-" * 55)
print(f"Total product types      : {len(inventory)}")
print(f"Total units in stock     : {total_stock}")
print(f"Total inventory value    : ₹{total_inventory_value}")
print(f"Most valuable product    : {most_valuable['name']}")
print(f"Highest inventory value  : ₹{most_valuable['value']}")
print("=" * 55)