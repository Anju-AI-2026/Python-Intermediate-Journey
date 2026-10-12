
# Batch Processing with Iterators

def process_batches(data, batch_size):

    if batch_size <= 0:
        raise ValueError("Batch size must be greater than zero.")

    data_iterator = iter(data)

    while True:
        batch = []

        for _ in range(batch_size):
            try:
                batch.append(next(data_iterator))
            except StopIteration:
                break

        if not batch:
            break

        yield batch


student_scores = [78, 92, 65, 88, 73, 95, 81, 69, 90]

print("STUDENT SCORE BATCH PROCESSOR")
print("-" * 35)

for batch_number, batch in enumerate(
    process_batches(student_scores, 3),
    start=1
):
    print(f"Batch {batch_number}: {batch}")
    print(f"Batch average: {sum(batch) / len(batch):.2f}")
    print("-" * 35)
