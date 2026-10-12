
# Manual Iterator Demonstration

subjects = ["Python", "DBMS", "Networking", "Mathematics"]

subject_iterator = iter(subjects)

print("SUBJECT ITERATOR")
print("-" * 30)

while True:
    try:
        subject = next(subject_iterator)
        print("Subject:", subject)

    except StopIteration:
        print("All subjects processed.")
        break
