import string

# Get password input
password = input("Enter a password to check: ")

# Check password characteristics
checks = {
    "At least 8 characters": len(password) >= 8,
    "Contains uppercase letters": any(c.isupper() for c in password),
    "Contains lowercase letters": any(c.islower() for c in password),
    "Contains digits": any(c.isdigit() for c in password),
    "Contains special characters": any(
        c in string.punctuation for c in password
    )
}

# Count successful checks
score = sum(checks.values())

# Determine strength
if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Moderate"
else:
    strength = "Weak"

# Display results
print("\n" + "=" * 45)
print("       🔐 PASSWORD STRENGTH CHECKER")
print("=" * 45)

for check, passed in checks.items():
    status = "Passed" if passed else "Not met"
    print(f"{check:<32}: {status}")

print("-" * 45)
print(f"Strength: {strength} ({score}/5 checks)")
print("=" * 45)