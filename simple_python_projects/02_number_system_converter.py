def convert_number(number):
    print("\n" + "=" * 40)
    print("       NUMBER CONVERSION RESULTS")
    print("=" * 40)

    print(f"Decimal:     {number}")
    print(f"Binary:      {bin(number)}")
    print(f"Octal:       {oct(number)}")
    print(f"Hexadecimal: {hex(number)}")

    print("=" * 40)


def main():
    print("=" * 40)
    print("       NUMBER SYSTEM CONVERTER")
    print("=" * 40)

    try:
        number = int(input("Enter a whole number: "))
        convert_number(number)

    except ValueError:
        print("Invalid input! Please enter a whole number.")


if __name__ == "__main__":
    main()