
# Log File Processor
# Demonstrates generator-based log filtering


def read_log_entries(log_entries):

    for entry in log_entries:
        yield entry


def filter_errors(log_entries):

    for entry in read_log_entries(log_entries):
        if "ERROR" in entry:
            yield entry


logs = [
    "INFO: Application started",
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "WARNING: High memory usage",
    "ERROR: Invalid configuration",
    "INFO: Application stopped",
]

print("=" * 55)
print("                LOG FILE PROCESSOR")
print("=" * 55)

error_count = 0

for error_number, entry in enumerate(filter_errors(logs), start=1):
    print(f"{error_number}. {entry}")
    error_count += 1

print("-" * 55)
print("Total errors found:", error_count)
print("=" * 55)

