
# Number Sequence Generator
# Demonstrates generators and the yield keyword


def number_generator(start, end):

    current = start

    while current <= end:
        yield current
        current += 1


print("=" * 40)
print("       NUMBER SEQUENCE GENERATOR")
print("=" * 40)

start = 1
end = 10

for number in number_generator(start, end):
    print(number)

print("=" * 40)
print("Sequence generation completed.")
