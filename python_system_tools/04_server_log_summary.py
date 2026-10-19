
# Server Log Summary Generator
# Summarizes log levels and identifies application errors

from collections import Counter
from pathlib import Path


def summarize_logs(file_path):
    path = Path(file_path)

    if not path.is_file():
        print(f"Error: Log file not found: {file_path}")
        return

    try:
        with path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
    except (OSError, UnicodeError) as error:
        print(f"Could not read log file: {error}")
        return

    levels = ("INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL")
    counts = Counter()
    errors = []
    unclassified = 0

    for line in lines:
        matched_level = None

        for level in levels:
            if f" {level} " in f" {line} ":
                counts[level] += 1
                matched_level = level
                break

        if matched_level is None:
            unclassified += 1
        elif matched_level in ("ERROR", "CRITICAL"):
            errors.append(line)

    print("\n" + "=" * 60)
    print("             SERVER LOG SUMMARY")
    print("=" * 60)
    print("File:", path.name)
    print("Total non-empty log entries:", len(lines))

    print("-" * 60)
    print("Log level counts:")

    for level in levels:
        print(f"{level:<12} | {counts[level]}")

    print(f"{'UNCLASSIFIED':<12} | {unclassified}")

    print("-" * 60)
    print("Error and critical messages:")

    if errors:
        for number, message in enumerate(errors, start=1):
            print(f"{number}. {message}")
    else:
        print("No ERROR or CRITICAL messages found.")

    print("-" * 60)
    print("Total error/critical messages:", len(errors))
    print("=" * 60)


if __name__ == "__main__":
    summarize_logs(input("Enter log file path: ").strip())
