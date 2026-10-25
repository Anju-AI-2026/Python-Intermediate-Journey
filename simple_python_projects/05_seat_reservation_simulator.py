def display_seats(seats):
    print("\n" + "=" * 35)
    print("         SEAT AVAILABILITY")
    print("=" * 35)

    for seat_number, is_booked in seats.items():
        status = "Booked" if is_booked else "Available"
        print(f"Seat {seat_number}: {status}")

    print("=" * 35)


def reserve_seat(seats):
    try:
        seat_number = int(input("Enter seat number to reserve: "))

        if seat_number not in seats:
            print("Invalid seat number.")
        elif seats[seat_number]:
            print("Sorry, this seat is already booked.")
        else:
            seats[seat_number] = True
            print(f"Seat {seat_number} reserved successfully!")

    except ValueError:
        print("Please enter a valid seat number.")


def cancel_reservation(seats):
    try:
        seat_number = int(input("Enter seat number to cancel: "))

        if seat_number not in seats:
            print("Invalid seat number.")
        elif not seats[seat_number]:
            print("This seat has not been booked.")
        else:
            seats[seat_number] = False
            print(f"Reservation for seat {seat_number} cancelled.")

    except ValueError:
        print("Please enter a valid seat number.")


def main():
    seats = {number: False for number in range(1, 11)}

    while True:
        print("\n" + "=" * 35)
        print("      SEAT RESERVATION SYSTEM")
        print("=" * 35)
        print("1. View Seats")
        print("2. Reserve a Seat")
        print("3. Cancel Reservation")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            display_seats(seats)
        elif choice == "2":
            reserve_seat(seats)
        elif choice == "3":
            cancel_reservation(seats)
        elif choice == "4":
            print("Thank you for using the reservation system!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()