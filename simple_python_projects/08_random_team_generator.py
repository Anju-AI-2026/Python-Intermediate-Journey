import random


def get_participants():
    participants = []

    try:
        count = int(input("How many participants are there? "))

        if count < 2:
            print("Please enter at least 2 participants.")
            return []

    except ValueError:
        print("Invalid input! Enter a whole number.")
        return []

    for number in range(1, count + 1):
        while True:
            name = input(f"Enter participant {number}'s name: ").strip()

            if not name:
                print("Name cannot be empty.")
            else:
                participants.append(name)
                break

    return participants


def generate_teams(participants, team_count):
    shuffled = participants.copy()
    random.shuffle(shuffled)

    teams = [[] for _ in range(team_count)]

    for index, participant in enumerate(shuffled):
        teams[index % team_count].append(participant)

    return teams


def main():
    print("=" * 40)
    print("       RANDOM TEAM GENERATOR")
    print("=" * 40)

    participants = get_participants()

    if not participants:
        return

    try:
        team_count = int(input("How many teams do you want? "))

        if team_count < 1 or team_count > len(participants):
            print(
                "The number of teams must be between "
                "1 and the number of participants."
            )
            return

    except ValueError:
        print("Invalid input! Enter a whole number.")
        return

    teams = generate_teams(participants, team_count)

    print("\n" + "=" * 40)
    print("           GENERATED TEAMS")
    print("=" * 40)

    for number, team in enumerate(teams, start=1):
        print(f"\nTeam {number}:")

        for participant in team:
            print(f"  - {participant}")

    print("\nTeams generated successfully!")
    print("=" * 40)


if __name__ == "__main__":
    main()