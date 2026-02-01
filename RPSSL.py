import random

options = ("rock", "paper", "scissors", "spock", "lizard")
player = None
com_win_number = 0
plyr_win_number = 0

while True:
    game_number = input("How many wins end the game?: ")
    if game_number.isdigit():
        game_number = int(game_number)
        break
    else:
        print("Please enter a number!")
while plyr_win_number < game_number and com_win_number < game_number:
    computer = random.choice(options)
    player = input("Please choose an option (rock, paper, scissors, spock, lizard) :").lower()
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "lizard" or computer == "scissors":
            print(f"The {player} crushes the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "spock":
            print(f"The {computer} vaporizes the {player}")
            print("Computer wins!")
            com_win_number +=1
        else:
            print(f"The {computer} covers the {player}")
            print("Computer wins!")
            com_win_number +=1
    elif player == "paper":
        if computer == "rock":
            print(f"The {player} covers the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "spock":
            print(f"The {player} disproves the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "scissors":
            print(f"The {computer} cuts the {player}")
            print("Computer wins!")
            com_win_number +=1
        else:
            print(f"The {computer} eats the {player}")
            print("Computer wins!")
            com_win_number +=1
    elif player == "scissors":
        if computer == "lizard":
            print(f"The {player} decapitates the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "paper":
            print(f"The {player} cuts the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "rock":
            print(f"The {computer} crushes the {player}")
            print("Computer wins!")
            com_win_number +=1
        else:
            print(f"The {computer} smashes the {player}")
            print("Computer wins!")
            com_win_number +=1
    elif player == "lizard":
        if computer == "paper":
            print(f"The {player} eats the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "spock":
            print(f"The {player} poisons the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "scissors":
            print(f"The {computer} decapitates the {player}")
            print("Computer wins!")
            com_win_number +=1
        else:
            print(f"The {computer} crushes the {player}")
            print("Computer wins!")
            com_win_number +=1
    elif player == "spock":
        if computer == "rock":
            print(f"The {player} vaporizes the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "scissors":
            print(f"The {player} smashes the {computer}")
            print("Player wins!")
            plyr_win_number +=1
        elif computer == "paper":
            print(f"The {computer} disproves the {player}")
            print("Computer wins!")
            com_win_number +=1
        else:
            print(f"The {computer} poisons the {player}")
            print("Computer wins!")
            com_win_number +=1

print("--------------End of the Game--------------")

print(f"Player: {plyr_win_number} , Computer: {com_win_number}")
if plyr_win_number < com_win_number:
    print("Computer wins the game!")
elif com_win_number < plyr_win_number:
    print("Player wins the game!")
print("-------------------------------------------")