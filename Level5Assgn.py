"""
#Level #5 Assignment - Rock Paper Scissors
#Create a Python game of Rock Paper Scissors.
Welcome the user to the game. Ask them how many rounds they would like to play. Ensure that
the number they enter is an odd number so there cannot be any ties.
For the game play, ask the user for their choice and then generate a random choice for the
computer. (NOTE: Make sure that the user’s choice is valid.) If there is a tie, the game does not
count, and we push to the next one. Keep track of the number of wins and losses for both the
player and the computer. When the game play is over, determine the overall winner and print the
results.
"""
#imports
import random

#global variables
player_wins = 0 
computer_wins = 0
ties = 0
round_count_current = 0

#functions
def get_player_choice():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input("Rock, Paper, or Scissors: ").lower()
        if choice not in valid_choices:
            print("Hmm, I didn't recognize your response. Please try again.")
        elif choice in valid_choices:
            break
        else:
            print("I'm sure sure what happened. Please try again.")
    return choice

def get_computer_choice():
    computer_choice = random.choice(["rock","paper","scissors"])
    print("The computer chose " + computer_choice + ".")
    return computer_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "player"
    elif player_choice == "rock" and computer_choice == "paper":
        return "computer"
    elif player_choice == "paper" and computer_choice == "rock":
        return "player"
    elif player_choice == "paper" and computer_choice == "scissors":
        return "computer"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "player"
    elif player_choice == "scissors" and computer_choice == "rock":
        return "computer"

#main game code
print("Let's play some Rock, Paper, Scissors") #welcome the user

while True: #get how many games and validate their response
    num_rounds = int(input("How many rounds would you like to play: ")) 
    if num_rounds % 2 == 0:
        print("You must put an odd number of games to play")
    elif num_rounds <= 0:
        print("Number of rounds must be positive and not zero")
    elif num_rounds > 16:
        sure = input("Are you sure? (yes/no) ")
        if sure == "yes" or sure == "Yes":
            break
        elif sure == "no" or sure == "No":
            print("Okay then")
        else:
            print("Not a valid input")
    elif num_rounds % 2 != 0 or num_rounds == 1:
        break

while num_rounds > round_count_current: #play the game
    player_choice = get_player_choice() #call the functions to get the player's choice
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    if result == "tie": 
        print("There was a tie! Play again.")
        ties += 1
    elif result == "player":
        print("You beat me!")
        player_wins += 1
        round_count_current += 1
    elif result == "computer":
        print("You lost")
        computer_wins += 1
        round_count_current += 1

#print out the results of the game
print("-----------------------------")
print(f"Scores - You: {player_wins}  Computer: {computer_wins}")
if player_wins > computer_wins:
    print("You won!!")
elif player_wins < computer_wins:
    print("The computer won!! Muhahahaha")
print("Thanks for playing")
