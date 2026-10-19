
# CSV Data Quality Checker
# Detects missing values and duplicate rows in CSV files

import csv
from collections import Counter
from pathlib import Path


def check_csv(file_path):
    path = Path(file_path)

    if not path.is_file():
        print(f"Error: File not found: {file_path}")
        return

    try:
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("Error: CSV file has no header.")
                return

            headers = reader.fieldnames

            if any(not header.strip() for header in headers):
                print("Error: CSV contains an empty column name.")
                return

            if len(set(headers)) != len(headers):
                print("Error: CSV contains duplicate column names.")
                return

            rows = list(reader)

    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Could not read CSV: {error}")
        return

    missing_values = Counter()
    normalized_rows = Counter()

    for row in rows:
        for column in headers:
            if not (row.get(column) or "").strip():
                missing_values[column] += 1

        row_key = tuple(
            (row.get(column) or "").strip()
            for column in headers
        )
        normalized_rows[row_key] += 1

    duplicate_groups = sum(
        count > 1 for count in normalized_rows.values()
    )
    duplicate_extra_rows = sum(
        count - 1
        for count in normalized_rows.values()
        if count > 1
    )

    print("\n" + "=" * 55)
    print("             CSV DATA QUALITY REPORT")
    print("=" * 55)
    print("File:", path.name)
    print("Columns:", len(headers))
    print("Data rows:", len(rows))
    print("Duplicate row groups:", duplicate_groups)
    print("Extra duplicate rows:", duplicate_extra_rows)

    print("-" * 55)
    print("Missing values by column:")

    for column in headers:
        print(f"{column:<25} | {missing_values[column]}")

    total_missing = sum(missing_values.values())
    print("-" * 55)
    print("Total missing values:", total_missing)

    if not rows:
        print("Note: CSV contains no data rows.")
    elif total_missing == 0 and duplicate_extra_rows == 0:
        print("Result: No missing values or duplicate rows found.")
    else:
        print("Result: Data cleaning may be required.")

    print("=" * 55)


if __name__ == "__main__":
    check_csv(input("Enter CSV file path: ").strip())
