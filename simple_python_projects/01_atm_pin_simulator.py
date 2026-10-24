def verify_pin(correct_pin):
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ").strip()

        if not entered_pin.isdigit() or len(entered_pin) != 4:
            print("Invalid PIN format. Enter exactly 4 digits.")
            continue

        if entered_pin == correct_pin:
            print("\nPIN verified successfully!")
            print("Welcome to the ATM.")
            return True

        attempts -= 1

        if attempts > 0:
            print("Incorrect PIN!")
            print(f"Attempts remaining: {attempts}")
        else:
            print("Too many incorrect attempts. Access locked.")

    return False


def main():
    correct_pin = "2468"

    print("=" * 35)
    print("          ATM SIMULATOR")
    print("=" * 35)

    if verify_pin(correct_pin):
        print("\nYou can now access your account.")
    else:
        print("\nPlease contact your bank for assistance.")


if __name__ == "__main__":
    main()