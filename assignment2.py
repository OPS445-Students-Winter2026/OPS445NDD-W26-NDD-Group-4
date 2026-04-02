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

                # Shows current points between players
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

                # Used to randomly get computer's choice randomly
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
def calculate_score(player , computer):
    if player == computer:
        print('Its a draw!\n\n')
        return random.choice([1, -1]) # randomly assign points
               
                # Check for winning conditions for player
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print('You win this round!\n')
        return 2
               
                # otherwise player loses
    else:
        print('You lose this round\n')
        return -1 
                
                #Main fucntion for the game
def main():
                #Set up for command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('points', type=int, help='Target score to win')
    args = parser.parse_args()

                #Validation for target score
    if not validate_points(args.points):
        print('Points must be greater than 2\n\n')
        return
    
                #Show instructions
    show_info()

                #Initial scores
    player_score = 0
    computer_score = 0

                #Game loop runs until someone reaches target score
    while player_score < args.points and computer_score < args.points:

                #Ask user for input, returns a copy of the string in lower case
        player_choice = input('Enter rock, paper or scissors: \n').lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print ('Invalid choice. Try again. rock, paper or scissors\n')
            continue #Restarts if invalid input
                
                #Computer choice
        computer_choice = get_computer_choice()

                #show countdown before revealing results
        countdown()
                
                #Dispay choices
        print(f"You chose: {player_choice}" )
        print(f"Computer chose: {computer_choice}\n")

                #calculate result of the round
        result = calculate_score(player_choice, computer_choice)

                #Update scores based on result
        if result == 2:
            player_score += 2 # Player wins
        elif result == -1:
            computer_score += 2 # computer wins
        else: #In case of a draw
            if result == 1:
                player_score += 1
            else:
                computer_score += 1
                
                #Display updated scores
        print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

                # Determine Winnner
    if player_score >= args.points:
        print("You win the game!\n\n")
        print("""
****************************************
*  *  *  *  *  *  *  *  *  *  *  *  *  *
*                                      *
*            YOU WIN!                  *
*                                      *
*  *  *  *  *  *  *  *  *  *  *  *  *  *
****************************************
""")
    else:
        print("Computer wins the game!\n\n")
        print("""
****************************************
*  *  *  *  *  *  *  *  *  *  *  *  *  *
*                                      *
*           COMPUTER WIN!              *
*                                      *
*  *  *  *  *  *  *  *  *  *  *  *  *  *
****************************************
""")


if __name__ == "__main__":
    main()