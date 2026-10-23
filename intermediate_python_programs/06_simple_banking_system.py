
def display_menu():
    print("\n" + "=" * 35)
    print("       SIMPLE BANKING SYSTEM")
    print("=" * 35)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 35)


def check_balance(balance):
    print(f"\nCurrent balance: ₹{balance:.2f}")


def deposit_money(balance):
    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            balance += amount
            print(f"₹{amount:.2f} deposited successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")

    return balance


def withdraw_money(balance):
    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")

    return balance


def main():
    balance = 1000.00

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit_money(balance)

        elif choice == "3":
            balance = withdraw_money(balance)

        elif choice == "4":
            print("\nThank you for using the banking system!")
            print(f"Final balance: ₹{balance:.2f}")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
