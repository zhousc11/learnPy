import random

computer = random.randint(0, 2)
player = input('Enter your choice (rock, paper, scissors): ')
if player == 'rock':
    player = 0
elif player == 'paper':
    player = 1
elif player == 'scissors':
    player = 2
else:
    print('Invalid choice!')
    exit()

if computer == 0:
    print('Computer: rock')
    if player == 0:
        print('Player: rock')
        print('Draw!')
    elif player == 1:
        print('Player: paper')
        print('Player wins!')
    elif player == 2:
        print('Player: scissors')
        print('Computer wins!')
elif computer == 1:
    print('Computer: paper')
    if player == 0:
        print('Player: rock')
        print('Computer wins!')
    elif player == 1:
        print('Player: paper')
        print('Draw!')
    elif player == 2:
        print('Player: scissors')
        print('Player wins!')
elif computer == 2:
    print('Computer: scissors')
    if player == 0:
        print('Player: rock')
        print('Player wins!')
    elif player == 1:
        print('Player: paper')
        print('Computer wins!')
    elif player == 2:
        print('Player: scissors')
        print('Draw!')
