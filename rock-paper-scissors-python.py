import random

choices = ["rock", "paper", "scissors"]

while True:
    player = input('rock, paper, scissors or exit: ').lower()

    if player == 'exit':
        print("Thanks for playing!")
        break
    if player not in choices:
        print("Choose rock, paper or scissors!")
        continue


    computer = random.choice(choices)
    print(f"You: {player}, computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    print("-" * 30)