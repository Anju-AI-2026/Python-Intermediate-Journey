
# Password Policy Auditor
# Checks passwords against configurable security rules

def audit_password(password):
    checks = {
        "Minimum 8 characters": len(password) >= 8,
        "Contains uppercase letter": any(
            char.isupper() for char in password
        ),
        "Contains lowercase letter": any(
            char.islower() for char in password
        ),
        "Contains a digit": any(
            char.isdigit() for char in password
        ),
        "Contains a special character": any(
            not char.isalnum() for char in password
        ),
    }

    print("\n" + "=" * 45)
    print("          PASSWORD AUDIT REPORT")
    print("=" * 45)

    for rule, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"{rule:<32} | {status}")

    passed_count = sum(checks.values())
    total_checks = len(checks)

    print("-" * 45)
    print(f"Rules passed: {passed_count}/{total_checks}")

    if passed_count == total_checks:
        print("Result: All policy checks passed.")
    else:
        print("Result: Password needs improvement.")

    print("=" * 45)


password = input("Enter a test password: ")
audit_password(password)
