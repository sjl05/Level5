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
Build and use at least two custom functions:
• get_player_choice: This function should prompt the player, convert the response to
lowercase, validate the choice, and return the result.
• determine_winner: This function should compare the two choices and return "win",
"loss", or "tie".
Sample Session:
Welcome to Rock Paper Scissors!
How many rounds would you like to play: 2
Sorry, the number must be an odd number. Please try again: 3
Enter rock, paper, scissors: sandwich
Sorry, “sandwich” is not a valid choice. Please try again.
Enter rock, paper, scissors: rock
The computer chose scissors.
You won!
Enter rock, paper, scissors: rock
The computer chose rock.
Tie! Play again.
Enter rock, paper, scissors: scissors
The computer chose rock.
You lost!
Enter rock, paper, scissors: paper
The computer chose rock.
You won!
-------------------------------------------
Score — You: 2 | Computer: 1
You win!!!
Thanks for playing!
Submit your PUBLIC GitHub link via Canvas.
"""
