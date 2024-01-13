import random

choices = ["rock", "paper", "scissors"]


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw!"
    elif (player_choice - computer_choice) % 3 == 1:
        return "Player wins!"
    else:
        return "Computer wins!"


while True:
    computer = random.randint(0, 2)
    player_input = input('Enter your choice (rock, paper, scissors) or "exit" to quit: ')

    if player_input == "exit":
        break

    if player_input in choices:
        player = choices.index(player_input)
        print(f"Computer: {choices[computer]}")
        print(f"Player: {player_input}")
        print(determine_winner(player, computer))
    else:
        print('Invalid choice! Please choose "rock", "paper", or "scissors".')
