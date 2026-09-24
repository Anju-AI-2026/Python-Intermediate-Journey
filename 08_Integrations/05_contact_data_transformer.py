# Store contact information
contacts = [
    {
        "name": "anju",
        "city": "hubli",
        "phone": "9876543210"
    },
    {
        "name": "ravi",
        "city": "dharwad",
        "phone": "8765432109"
    },
    {
        "name": "rossy",
        "city": "bangalore",
        "phone": "7654321098"
    },
    {
        "name": "arjun",
        "city": "mysore",
        "phone": "6543210987"
    }
]


# Transform contact information
formatted_contacts = list(
    map(
        lambda contact: {
            "name": contact["name"].title(),
            "city": contact["city"].title(),
            "phone": "+91 " + contact["phone"]
        },
        contacts
    )
)


# Display original contacts
print("\n" + "=" * 50)
print("          📱 CONTACT DATA TRANSFORMER")
print("=" * 50)

print("\n📋 ORIGINAL CONTACTS")
print("-" * 50)

for contact in contacts:
    print(
        f"{contact['name']:<10} "
        f"{contact['city']:<12} "
        f"{contact['phone']}"
    )


# Display transformed contacts
print("\n✨ FORMATTED CONTACTS")
print("-" * 50)

for contact in formatted_contacts:
    print(
        f"{contact['name']:<10} "
        f"{contact['city']:<12} "
        f"{contact['phone']}"
    )


# Display summary
print("\n📊 SUMMARY")
print("-" * 50)
print(f"Total contacts : {len(formatted_contacts)}")
print("=" * 50)