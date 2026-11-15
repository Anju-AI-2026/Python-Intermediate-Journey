# Number Guessing Game

## 📌 Project Overview

A simple interactive Python game where the player tries to guess a randomly generated number between 1 and 100 within a limited number of attempts.

The game provides hints after each guess and allows the player to play multiple rounds.

## ✨ Features

- Generates a random number between 1 and 100.
- Provides 7 attempts to guess the correct number.
- Displays hints such as "Too high" and "Too low".
- Validates guesses to ensure they are within the allowed range.
- Handles invalid inputs using exception handling.
- Displays the number of attempts used when the player wins.
- Allows the player to restart the game.

## 🧠 Concepts Practiced

- Python functions
- `random` module
- `while` loops
- Conditional statements
- User input and type conversion
- Input validation
- Exception handling using `try-except`
- String formatting
- Program control using `return` and `break`

## 🛠️ Technologies Used

- Python 3
- Python standard library

## ▶️ How to Run

Open a terminal in the repository directory and execute:

```bash
python intermediate_python_programs/01_number_guessing_game.py
```

## 🎮 Sample Output

```text
========================================
       NUMBER GUESSING GAME
========================================
Guess a number between 1 and 100.
You have 7 attempts!

Enter your guess: 40
Too low! Try a higher number.
Attempts remaining: 6

Enter your guess: 70
Too high! Try a lower number.
Attempts remaining: 5

Enter your guess: 55
Correct! You won in 3 attempts!

Would you like to play again? (yes/no):
```

*Note: The secret number and hints depend on the randomly generated number and the player's guesses.*

## 🎯 Purpose

To practice Python fundamentals by building an interactive guessing game with random number generation, input validation, loops, and exception handling.