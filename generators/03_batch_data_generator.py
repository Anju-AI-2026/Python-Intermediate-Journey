
# Batch Data Generator
# Generates records in smaller batches


def generate_batches(records, batch_size):

    if batch_size <= 0:
        raise ValueError("Batch size must be greater than zero.")

    batch = []

    for record in records:
        batch.append(record)

        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


student_records = [
    {"name": "Asha", "score": 82},
    {"name": "Meera", "score": 76},
    {"name": "Anji", "score": 95},
    {"name": "Priya", "score": 68},
    {"name": "Sneha", "score": 88},
    {"name": "Kavya", "score": 91},
    {"name": "Riya", "score": 73},
]

print("=" * 45)
print("          BATCH DATA GENERATOR")
print("=" * 45)

batch_number = 0

for batch_number, batch in enumerate(
    generate_batches(student_records, 3),
    start=1
):
    print(f"\nBatch {batch_number}")

    for record in batch:
        print(f"{record['name']:<10} | Score: {record['score']}")

    average = sum(record["score"] for record in batch) / len(batch)
    print(f"Batch average: {average:.2f}")

print("\nTotal batches processed:", batch_number)
print("=" * 45)
