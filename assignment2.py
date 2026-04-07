#OPS445 Assignment 2 
#Group 4 -  Tahsin Absar - Franz Rosete

#!/usr/bin/env python3

# import required modules
import argparse # argparse is used to handle command-line arguments
import random   # used for the computer random choice and draw scoring
import time     # used for countdown delay hehe

# Shows game information to user and instructions
def show_info():
    print('Rock Paper Scissors Game')
    print('How it works:')
    print('The computer randomly selects a number from 1 to 3.')
    print('1 = rock, 2 = paper, 3 = scissors.')
    print('You enter rock, paper, or scissors each round.')
    print('Scoring system:')
    print('   - Win = 2 points')
    print('   - Loss = -1 point')
    print('   - Draw = randomly gives either player 1 point')
    print('First player to reach the target score wins.')

# Checks if the number of points to win the game argument is greater than 2. If yes return true
def validate_points(points):
    return points > 2

# converts numbers 1 - 3 into rock, paper or scissors
def number_to_choose(number):
    if number == 1:
        return 'rock'
    elif number == 2:
        return 'paper'
    else:
        return 'scissors'
    
# Function to get valid user input
def get_user_choice():

    # Ask user for input (automatically changes to lowercase even if user inputs uppercase)
    choice = input("Enter rock, paper, or scissors: ").lower()

    # Keep asking until valid
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("Invalid choice. Try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()

    return choice

# Used to get computer's choice randomly using randint
def get_computer_choice():
    random_number = random.randint(1, 3)
    return number_to_choose(random_number)

# countdown before revealing choices (adds game feel)
def countdown():
    print('\nRock...')
    time.sleep(0.5)  # Pause for half a second
    print('Paper...')
    time.sleep(0.5)
    print('Scissors...')
    time.sleep(0.5)
    print('SHOOT!\n')
    time.sleep(0.3)
                
# Used to determine the result of a round and returns score         
def get_result(player, computer):
    if player == computer:
        return "draw"
    elif player == "rock" and computer == "scissors":
        return "win"
    elif player == "paper" and computer == "rock":
        return "win"
    elif player == "scissors" and computer == "paper":
        return "win"
    else:
        return "loss"
    

                
#Main fucntion for the game
def main():

# This section sets up command-line arguments using argparse.
# It allows the user to run the program with inputs directly from the terminal which we will use for our game
# - "-i" is an argument that displays the game information about how the game is played. (Optional)
# - "points" is an integer argument that represents the target score needed to win the game.
# - "choice" is an argument where the user enters their move, in this case - rock, paper, or scissors.
#
# The parser reads the user’s input from the command line and stores the values in the variable called "args",
# which we can then use throughout the program (e.g., args.i, args.points, args.choice).

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", action="store_true", help="show game info")
    parser.add_argument("points", nargs="?", type=int, help="target score")
    parser.add_argument("choice", nargs="?", help="rock, paper, or scissors")

    args = parser.parse_args()

    # Show info and exit
    if args.i:
        show_info()
        return

    # Check missing arguments
    if args.points is None or args.choice is None:
        print("Usage: python3 rps.py <points> <rock|paper|scissors>")
        return

    # Validate points
    if not validate_points(args.points):
        print("Points must be greater than 2")
        return

    # Validate choice
    if args.choice not in ["rock", "paper", "scissors"]:
        print("Choice must be rock, paper, or scissors")
        return

    # Initialize scores
    player_score = 0
    computer_score = 0

    # First round uses argument
    player_choice = args.choice

    # Game loop
    while player_score < args.points and computer_score < args.points:

        computer_choice = get_computer_choice()

        countdown()

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)

        result = get_result(player_choice, computer_choice)

        #Scoring System Logic:
        if result == "win":
            print("You win this round!")

            player_score += 2

            if computer_score > 0:
                computer_score -= 1

        elif result == "loss":
            print("You lose this round!")

            computer_score += 2

            if player_score > 0:
                player_score -= 1

        else:
            print("It is a draw!")

            if random.randint(1, 2) == 1:
                print("You get 1 point from the draw!")
                player_score += 1
            else:
                print("Computer gets 1 point from the draw!")
                computer_score += 1

        # Show scores
        print("Score -> You:", player_score, "| Computer:", computer_score)
        print()

        # Next round input
        if player_score < args.points and computer_score < args.points:
            player_choice = get_user_choice()

    # Final winner
    if player_score >= args.points:
        print("You win the game!")
    else:
        print("Computer wins the game!")

if __name__ == "__main__":
    main()
