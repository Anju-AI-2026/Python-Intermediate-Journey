def calculate_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    return bill


def main():
    print("=" * 40)
    print("       ELECTRICITY BILL CALCULATOR")
    print("=" * 40)

    try:
        units = float(input("Enter electricity units consumed: "))

        if units < 0:
            print("Units cannot be negative.")
            return

        bill = calculate_bill(units)

        print("\nBILL DETAILS")
        print("-" * 40)
        print(f"Units consumed: {units:.2f}")
        print(f"Total bill:     Rs. {bill:.2f}")
        print("-" * 40)

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()