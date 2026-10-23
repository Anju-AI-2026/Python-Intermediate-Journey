
import random


CHOICES = ["rock", "paper", "scissors"]


def decide_winner(player, computer):
    if player == computer:
        return "tie"

    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if winning_moves[player] == computer:
        return "player"

    return "computer"


def main():
    player_score = 0
    computer_score = 0
    ties = 0

    print("=" * 42)
    print("          ROCK PAPER SCISSORS")
    print("=" * 42)

    while True:
        player = input(
            "\nChoose rock, paper, or scissors (or quit): "
        ).strip().lower()

        if player == "quit":
            break

        if player not in CHOICES:
            print("Invalid choice! Please try again.")
            continue

        computer = random.choice(CHOICES)

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        result = decide_winner(player, computer)

        if result == "player":
            print("You win this round!")
            player_score += 1

        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("It's a tie!")
            ties += 1

        print(
            f"Score — You: {player_score} | "
            f"Computer: {computer_score} | Ties: {ties}"
        )

    print("\n" + "=" * 42)
    print("             FINAL SCORE")
    print("=" * 42)
    print(f"Your wins:     {player_score}")
    print(f"Computer wins: {computer_score}")
    print(f"Ties:          {ties}")

    if player_score > computer_score:
        print("Overall result: You won!")
    elif computer_score > player_score:
        print("Overall result: Computer won!")
    else:
        print("Overall result: It's a tie!")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
