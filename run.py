# Import necessary modules
import random
import os
from art import logo
from simple_term_menu import TerminalMenu

#CONSTANTS 
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 5
CODE_LENGTH = 4

def main_menu():
    """
    Displays the menu. 
    Rules 
    Start - With levels later
    Quit
    """
    # Define menu items
    menu_items = ["Rules of MasterMind", "Start MasterMind", "Quit"]
    # Create a menu object
    menu = TerminalMenu(menu_items)
    # Show the menu and get the user's selection
    menu_entry_index = menu.show()

    # Handle user selection
    if menu_entry_index == 0:
        input("Press any key to return to menu.")
    elif menu_entry_index == 1:
        game()
    elif menu_entry_index == 2:
        quit()

def generate_code():
    """
    Generates a random code by selecting a color 
    from the COLORS list for each position in the
    code and then returning the code.

    This need a rewrite.
    """
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    """
    Player / Users guess. 
    """
    guess = []
    for _ in range(CODE_LENGTH):
        while True:
            color = input(f"Guess color {_ + 1}: ").upper()
            if color in COLORS:
                guess.append(color)
                print(f"[{''.join(guess)}{'-' * (CODE_LENGTH - len(guess))}]")
                break
            else:
                print(f"Invalid color: {color}. Try again.")
    return guess

def check_code(guess, real_code):
    """
    Checks code 'guess' against 'real_code' 
    USE ZIP! Go back to lovesandwich.    
    """
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count occurrences of each color in the real code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    # Print feedback on the guess Clear screen
    os.system('clear')
    print(f"Guess: {guess} | Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}.")

def game():
    """
    HERE BE GAME!
    """
    os.system('clear')
    print(logo)
    print(f"Welcome to MasterMind. \nYou have {TRIES} tries to guess the code using {CODE_LENGTH} colors...")
    print("The valid colors are", *COLORS)


    main_menu()

    real_code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        check_code(guess, real_code)

        if sorted(guess) == sorted(real_code):
            print(f"You guessed the code in {attempts} tries!\n A real MasterMind")
            break

    else:
        print("You ran out of tries, the code was", *real_code)


# Main entry point of the program
if __name__ == "__main__":
    game()

