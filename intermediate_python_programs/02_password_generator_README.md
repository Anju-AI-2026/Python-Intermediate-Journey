# Password Generator

## 📌 Project Overview

A Python program that generates random passwords based on the user's preferences. Users can choose the password length and decide whether to include digits and special symbols.

## ✨ Features

- Generates passwords using uppercase and lowercase letters.
- Allows users to select a password length between 1 and 128 characters.
- Provides an option to include digits.
- Provides an option to include special symbols.
- Validates user choices.
- Handles invalid numerical input using exception handling.
- Generates passwords according to the selected preferences.

## 🧠 Concepts Practiced

- Python functions
- `random` module
- `string` module
- String concatenation
- Conditional statements
- User input and type conversion
- Input validation
- Exception handling using `try-except`
- List-free string generation using `join()`
- Generator expressions
- Main function and `if __name__ == "__main__"`

## 🛠️ Technologies Used

- Python 3
- Python standard library

## ▶️ How to Run

Open a terminal in the repository directory and execute:

```bash
python intermediate_python_programs/02_password_generator.py
```

## 🔐 Sample Output

```text
========================================
        PASSWORD GENERATOR
========================================
Enter password length: 12
Include digits? (y/n): y
Include symbols? (y/n): y

Your generated password:
aB7@kP2#mX9!
```

*Note: The generated password will be different each time.*

## 🎯 Purpose

To understand random password generation, string manipulation, conditional character selection, and input validation through a practical Python program.

## ⚠️ Note

This project uses Python's `random` module for learning purposes. For real-world security-sensitive password generation, Python's `secrets` module is recommended.