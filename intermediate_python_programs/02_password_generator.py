
import random
import string


def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    password = "".join(
        random.choice(characters) for _ in range(length)
    )

    return password


def main():
    print("=" * 40)
    print("        PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))

        if not 1 <= length <= 128:
            print("Please choose a length between 1 and 128.")
            return

        digits_choice = input("Include digits? (y/n): ").strip().lower()
        symbols_choice = input("Include symbols? (y/n): ").strip().lower()

        if digits_choice not in ("y", "n") or symbols_choice not in ("y", "n"):
            print("Please enter only 'y' or 'n'.")
            return

        password = generate_password(
            length,
            digits_choice == "y",
            symbols_choice == "y"
        )

        print("\nYour generated password:")
        print(password)

    except ValueError:
        print("Invalid input! Please enter a whole number for length.")


if __name__ == "__main__":
    main()
