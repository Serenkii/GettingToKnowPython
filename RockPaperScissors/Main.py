import random


def print_score():
    print(f"Wins: {wins}")
    print(f"Draws: {draws}")
    print(f"Losses: {losses}")


possibilities = ("rock", "paper", "scissors")

wins = 0
draws = 0
losses = 0

while True:
    print("Rock, paper, scissors!")
    user_input = str(input())
    random_choice = possibilities[random.randint(0, 2)]

    if user_input == "0":
        print_score()
        break
    elif user_input == "score":
        print_score()
        continue
    elif (user_input.lower() == "rock" and random_choice == "scissors") \
            or (user_input.lower() == "paper" and random_choice == "rock") \
            or (user_input.lower() == "scissors" and random_choice == "paper"):
        print("You win!")
        wins += 1
    elif (user_input.lower() == "rock" and random_choice == "paper") \
            or (user_input.lower() == "paper" and random_choice == "scissors") \
            or (user_input.lower() == "scissors" and random_choice == "rock"):
        print("You loose!")
        losses += 1
    elif user_input.lower() == random_choice:
        print("It's a draw!")
        draws += 1
    else:
        print(f"Your input was incorrect. (\"{user_input}\")")
        continue

    print(f"You chose {user_input.lower().capitalize()} and your enemy chose {random_choice.capitalize()}.\n")
