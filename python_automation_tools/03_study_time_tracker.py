from collections import defaultdict

# Store study sessions
sessions = []

# Collect study information
session_count = int(input("How many study sessions? "))

for number in range(session_count):
    print(f"\nSession {number + 1}")

    subject = input("Subject: ").strip()
    hours = float(input("Study hours: "))

    if not subject or hours <= 0:
        print("Invalid session. Please enter valid details.")
        continue

    sessions.append({
        "subject": subject,
        "hours": hours
    })

# Calculate total hours by subject
subject_hours = defaultdict(float)

for session in sessions:
    subject_hours[session["subject"]] += session["hours"]

total_hours = sum(subject_hours.values())

# Find the most-studied subject
if subject_hours:
    top_subject = max(subject_hours, key=subject_hours.get)
else:
    top_subject = "None"

# Display report
print("\n" + "=" * 45)
print("         📚 STUDY TIME REPORT")
print("=" * 45)

for subject, hours in sorted(subject_hours.items()):
    print(f"{subject:<25} {hours:.2f} hours")

print("-" * 45)
print(f"Sessions recorded : {len(sessions)}")
print(f"Total study time  : {total_hours:.2f} hours")
print(f"Most-studied      : {top_subject}")
print("=" * 45)