def calculate_discount(subtotal):
    if subtotal >= 5000:
        return subtotal * 0.10
    elif subtotal >= 2000:
        return subtotal * 0.05
    return 0


def main():
    cart = []

    print("=" * 45)
    print("          SHOPPING BILL GENERATOR")
    print("=" * 45)

    while True:
        name = input("\nEnter product name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            break

        if not name:
            print("Product name cannot be empty.")
            continue

        try:
            price = float(input("Enter price per item: Rs. "))
            quantity = int(input("Enter quantity: "))

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be greater than zero.")
                continue

            cart.append({
                "name": name,
                "price": price,
                "quantity": quantity,
                "total": price * quantity
            })

            print("Product added successfully!")

        except ValueError:
            print("Invalid input! Enter a valid price and whole-number quantity.")

    if not cart:
        print("\nYour cart is empty. No bill generated.")
        return

    subtotal = sum(item["total"] for item in cart)
    discount = calculate_discount(subtotal)
    final_total = subtotal - discount

    print("\n" + "=" * 55)
    print("                    SHOPPING BILL")
    print("=" * 55)
    print(f"{'Product':<20}{'Price':>10}{'Qty':>6}{'Total':>12}")
    print("-" * 55)

    for item in cart:
        print(
            f"{item['name'][:20]:<20}"
            f"{item['price']:>10.2f}"
            f"{item['quantity']:>6}"
            f"{item['total']:>12.2f}"
        )

    print("-" * 55)
    print(f"{'Subtotal:':>40} Rs. {subtotal:>10.2f}")
    print(f"{'Discount:':>40} Rs. {discount:>10.2f}")
    print(f"{'Final Total:':>40} Rs. {final_total:>10.2f}")
    print("=" * 55)


if __name__ == "__main__":
    main()