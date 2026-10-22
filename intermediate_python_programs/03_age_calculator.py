
from datetime import date
import calendar


def calculate_age(birth_date, current_date):
    if birth_date > current_date:
        raise ValueError("Date of birth cannot be in the future.")

    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    if days < 0:
        months -= 1

        previous_month = current_date.month - 1
        previous_year = current_date.year

        if previous_month == 0:
            previous_month = 12
            previous_year -= 1

        days_in_previous_month = calendar.monthrange(
            previous_year, previous_month
        )[1]

        days += days_in_previous_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def main():
    print("=" * 40)
    print("           AGE CALCULATOR")
    print("=" * 40)

    try:
        birth_year = int(input("Enter birth year: "))
        birth_month = int(input("Enter birth month (1-12): "))
        birth_day = int(input("Enter birth day: "))

        birth_date = date(birth_year, birth_month, birth_day)
        current_date = date.today()

        years, months, days = calculate_age(
            birth_date, current_date
        )

        print("\nYour age:")
        print(f"{years} years, {months} months, {days} days")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
