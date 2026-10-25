import random

CHOICES = ["rock", "paper", "scissors"]

def find_winner(player, computer):
    if player == computer:
        return "tie"

    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_moves[player] == computer:
        return "player"

    return "computer"


def main():
    player_score = 0
    computer_score = 0
    ties = 0

    print("=" * 40)
    print("     ROCK-PAPER-SCISSORS TOURNAMENT")
    print("=" * 40)

    try:
        rounds = int(input("How many rounds do you want to play? "))

        if rounds <= 0:
            print("Please enter a positive number of rounds.")
            return

    except ValueError:
        print("Invalid input! Enter a whole number.")
        return

    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} of {rounds} ---")

        while True:
            player = input(
                "Choose rock, paper, or scissors: "
            ).strip().lower()

            if player in CHOICES:
                break

            print("Invalid choice! Please try again.")

        computer = random.choice(CHOICES)

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        winner = find_winner(player, computer)

        if winner == "player":
            print("You won this round!")
            player_score += 1

        elif winner == "computer":
            print("Computer won this round!")
            computer_score += 1

        else:
            print("This round is a tie!")
            ties += 1

        print(
            f"Score: You {player_score} - "
            f"{computer_score} Computer | Ties: {ties}"
        )

    print("\n" + "=" * 40)
    print("          TOURNAMENT RESULTS")
    print("=" * 40)
    print(f"Your wins: {player_score}")
    print(f"Computer wins: {computer_score}")
    print(f"Ties: {ties}")

    if player_score > computer_score:
        print("Congratulations! You won the tournament!")
    elif computer_score > player_score:
        print("The computer won the tournament!")
    else:
        print("The tournament ended in a tie!")

    print("=" * 40)


if __name__ == "__main__":
    main()