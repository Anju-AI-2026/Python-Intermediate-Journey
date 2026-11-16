# Simple Banking System

## 📌 Project Overview

A menu-driven Python banking application that allows users to check their account balance, deposit money, and withdraw money.

The program starts with an initial balance of ₹1,000 and updates the balance based on the user's transactions.

## ✨ Features

- Displays an interactive banking menu.
- Allows users to check their current balance.
- Supports money deposits.
- Supports money withdrawals.
- Prevents zero or negative transaction amounts.
- Checks for insufficient balance before withdrawals.
- Validates numerical input.
- Updates and maintains the account balance during execution.
- Displays the final balance when exiting the application.

## 🧠 Concepts Practiced

- Python functions
- Function parameters and return values
- Variables and arithmetic operations
- Conditional statements
- Infinite `while` loops
- Menu-driven programming
- User input and string methods
- Input validation
- Exception handling using `try-except`
- Floating-point numbers
- Formatted string output

## 🛠️ Technologies Used

- Python 3
- Python standard library

## ▶️ How to Run

Open a terminal in the repository directory and execute:

```bash
python intermediate_python_programs/06_simple_banking_system.py
```

## 🏦 Sample Output

```text
===================================
       SIMPLE BANKING SYSTEM
===================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
===================================
Enter your choice (1-4): 2
Enter deposit amount: ₹500
₹500.00 deposited successfully!

Enter your choice (1-4): 1
Current balance: ₹1500.00

Enter your choice (1-4): 4

Thank you for using the banking system!
Final balance: ₹1500.00
```

*Note: This is a basic simulation. The account balance is stored in memory and resets to ₹1,000 whenever the program is restarted.*

## 🎯 Purpose

To practice functions, menu-driven programming, transaction processing, input validation, and exception handling through a simple banking simulation.