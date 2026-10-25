def display_habits(habits):
    print("\n" + "=" * 40)
    print("          YOUR DAILY HABITS")
    print("=" * 40)

    if not habits:
        print("No habits added yet.")
        return

    for number, habit in enumerate(habits, start=1):
        status = "Completed" if habit["completed"] else "Pending"
        print(f"{number}. {habit['name']} - {status}")

    completed = sum(1 for habit in habits if habit["completed"])
    total = len(habits)

    print("-" * 40)
    print(f"Progress: {completed}/{total} habits completed")

    if total > 0:
        percentage = (completed / total) * 100
        print(f"Completion rate: {percentage:.1f}%")


def add_habit(habits):
    name = input("Enter the habit name: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return

    for habit in habits:
        if habit["name"].lower() == name.lower():
            print("This habit already exists.")
            return

    habits.append({"name": name, "completed": False})
    print(f"'{name}' added successfully!")


def complete_habit(habits):
    if not habits:
        print("No habits available. Add a habit first.")
        return

    display_habits(habits)

    try:
        number = int(input("Enter the habit number to mark complete: "))

        if number < 1 or number > len(habits):
            print("Invalid habit number.")
            return

        habit = habits[number - 1]

        if habit["completed"]:
            print("This habit is already completed!")
        else:
            habit["completed"] = True
            print(f"Great job! '{habit['name']}' completed!")

    except ValueError:
        print("Please enter a valid whole number.")


def remove_habit(habits):
    if not habits:
        print("No habits available to remove.")
        return

    display_habits(habits)

    try:
        number = int(input("Enter the habit number to remove: "))

        if number < 1 or number > len(habits):
            print("Invalid habit number.")
            return

        removed = habits.pop(number - 1)
        print(f"'{removed['name']}' removed successfully!")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    habits = [
        {"name": "Drink enough water", "completed": False},
        {"name": "Read for 20 minutes", "completed": False},
        {"name": "Exercise", "completed": False}
    ]

    while True:
        print("\n" + "=" * 40)
        print("           DAILY HABIT TRACKER")
        print("=" * 40)
        print("1. View habits and progress")
        print("2. Add a habit")
        print("3. Mark a habit as completed")
        print("4. Remove a habit")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_habits(habits)

        elif choice == "2":
            add_habit(habits)

        elif choice == "3":
            complete_habit(habits)

        elif choice == "4":
            remove_habit(habits)

        elif choice == "5":
            print("Keep building good habits. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()