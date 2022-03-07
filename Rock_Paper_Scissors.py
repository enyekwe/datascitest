# 21. ROCK, PAPER, SCISSORS GAME

# This program lets user play the game of Rock, Paper, and
# Scissors against the computer
import random
# computer generates a random number in the range of 1 to 3
##rock = 1
##paper = 2
##scissors = 3
another = 'y'
def main():
    # Call on the global variable
    global another
    # A while loop is generated to create choices
    while another == 'y':
        # Computer choice is generated
        comp_choice = comp_input()
        # User is prompted for input
        user_choice = get_user_input()
        while user_choice == comp_choice:
            print ()
            print ('It is a tie')
            print ()
            # Computer choice is generated
            comp_choice = comp_input()
            # User is prompted for input
            user_choice = get_user_input()
        # Computer's choice is displayed
        print()
        print("Computer's choice is", comp_choice)
        print()
        
        # Determine winner
        ##    if user_choice == comp_choice:   # Replace with if loop
        ##        print ('It is a tie')
        ##        print ()
        ##        main ()
        ##    else:
        winner_selector(user_choice, comp_choice)
    
        # Prompt user if they want to play again
        another = input('Do you want to play again?\nEnter "y" \
for yes and "n" for no: ')
        print()
##        if another == 'y':       # Replace with if loop
##            main()
##        else:
##            print()
##            print('Thank you for playing, I hope to see you soon')
        if another == 'n':
            print('Thank you for playing, I hope to see you soon')
            print()   

# This function generates a random number for the computer,
# assigns, and returns the computer's choice
def comp_input():
    #import random
    # Random number is generated for the computer
    comp_number = random.randint(1,4)
    # The number is assigned to its respective string
    if comp_number == 1:
        comp_selection = 'rock'
    elif comp_number == 2:
        comp_selection = 'paper'
    elif comp_number == 3:
        comp_selection = 'scissors'
    # The computer's choice is returned
    return comp_selection

# This function prompts for, validates and returns users input
def get_user_input ():
    # User is prompted to make his choice
    user_choice = input('Enter either rock, paper or scissors: ')

    # Users input is validated
    while user_choice != 'rock' and user_choice != 'paper'\
          and user_choice != 'scissors':
        print('Incorrect input')
        print()
        user_choice = input('Enter either rock, paper or scissors: ')
    return user_choice

# This function has the rules and decides the winner
def winner_selector(user_choice, comp_choice):
    if user_choice == 'rock' and comp_choice == 'scissors':
        print('Congratulations!!, you win')
        print('(Rock smashes scissors.)')
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print('Congratulations!!, you win')
        print('(Scissors cuts paper.)')
    elif user_choice == 'paper' and comp_choice == 'rock':
        print('Congratulations!!, you win')
        print('(Paper wraps rock.)')
    elif comp_choice == 'rock' and user_choice == 'scissors':
        print('Computer wins')
        print('(Rock smashes scissors.)')
    elif comp_choice == 'scissors' and user_choice == 'paper':
        print('Computer wins')
        print('(Scissors cuts paper.)')
    elif comp_choice == 'paper' and user_choice == 'rock':
        print('Computer wins')
        print('(Paper wraps rock.)')
    print()
main()
