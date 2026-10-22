
import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 7

    print("\n" + "=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)
    print("Guess a number between 1 and 100.")
    print(f"You have {attempts} attempts!")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            if not 1 <= guess <= 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts -= 1

            if guess == secret_number:
                print(f"\nCorrect! You won in {7 - attempts} attempts!")
                return

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

            print(f"Attempts remaining: {attempts}")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    print(f"\nGame over! The number was {secret_number}.")


while True:
    play_game()

    choice = input("\nWould you like to play again? (yes/no): ")
    if choice.strip().lower() not in ("yes", "y"):
        print("\nThanks for playing!")
        break
