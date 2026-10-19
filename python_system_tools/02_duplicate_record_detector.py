
# Duplicate Record Detector
# Identifies repeated records and counts their occurrences

from collections import Counter


def detect_duplicates(records):
    record_counts = Counter(records)
    duplicates = {
        record: count
        for record, count in record_counts.items()
        if count > 1
    }

    return duplicates


records = [
    "student_101",
    "student_102",
    "student_103",
    "student_101",
    "student_104",
    "student_102",
    "student_105",
    "student_101",
    "student_106",
]

duplicates = detect_duplicates(records)

print("=" * 50)
print("          DUPLICATE RECORD DETECTOR")
print("=" * 50)

print("Total records:", len(records))
print("Unique records:", len(set(records)))
print("Duplicate record types:", len(duplicates))

print("-" * 50)

if duplicates:
    print("Duplicate records found:")

    for record, count in duplicates.items():
        print(f"{record:<20} | Occurrences: {count}")
else:
    print("No duplicate records found.")

print("=" * 50)
