# Store habit information
habits = [
    {"name": "Study Python", "completed": 6, "target": 7},
    {"name": "Read Books", "completed": 4, "target": 7},
    {"name": "Exercise", "completed": 5, "target": 7},
    {"name": "Practice SQL", "completed": 3, "target": 7},
    {"name": "Revise Math", "completed": 7, "target": 7}
]


# Calculate habit progress
habit_records = list(
    map(
        lambda habit: {
            **habit,
            "percentage": round(
                habit["completed"] / habit["target"] * 100, 2
            ),
            "remaining": habit["target"] - habit["completed"]
        },
        habits
    )
)


# Find habits below 70% completion
needs_attention = list(
    filter(
        lambda habit: habit["percentage"] < 70,
        habit_records
    )
)


# Calculate overall completion
total_completed = sum(
    habit["completed"] for habit in habit_records
)

total_target = sum(
    habit["target"] for habit in habit_records
)

overall_percentage = round(
    total_completed / total_target * 100, 2
)


# Find the most consistent habit
best_habit = max(
    habit_records,
    key=lambda habit: habit["percentage"]
)


# Display report
print("\n" + "=" * 55)
print("             📅 HABIT TRACKER")
print("=" * 55)

print("\n📋 HABIT PROGRESS")
print("-" * 55)

for habit in habit_records:
    print(
        f"{habit['name']:<18} "
        f"{habit['completed']}/{habit['target']} "
        f"({habit['percentage']}%)"
    )


print("\n⚠️ HABITS NEEDING ATTENTION")
print("-" * 55)

for habit in needs_attention:
    print(
        f"{habit['name']:<18} "
        f"Remaining: {habit['remaining']} days"
    )


print("\n📊 WEEKLY SUMMARY")
print("-" * 55)
print(f"Total habits       : {len(habit_records)}")
print(f"Completed days    : {total_completed}")
print(f"Target days       : {total_target}")
print(f"Overall completion: {overall_percentage}%")
print(f"Most consistent   : {best_habit['name']}")
print("=" * 55)