# Import necessary modules
import random
import os
from art import logo, win
from simple_term_menu import TerminalMenu

#CONSTANTS 
# Define the colors used in the game
COLORS = ["R", "G", "B", "Y", "W", "O"]

def print_welcome_message():
    """
    Display a welcome message
    """
    os.system('clear')
    print(logo)
    print("Welcome to MasterMind Python Edition.")
    print("Select an option from the menu below:")

print_welcome_message()

def display_rules():
    """
    Display the rules of the game
    """
    os.system('clear')
    print("Rules for MasterMind:")
    print("1. The computer will generate a secret code consisting of a sequence of colors.")
    print("2. Your task is to guess the code.")
    print("3. You have a limited number of tries to guess the code.")
    print("4. After each guess, you will receive feedback on the correctness of your guess.")
    print("   - 'Correct Positions' indicates the number of colors in the correct positions.")
    print("   - 'Incorrect Positions' indicates the number of correct colors in the wrong positions.")
    print("5. The game ends when you correctly guess the code or run out of tries.")
    print("   The colors are Red, Green, Blue, Yellow, White and Orange.")
    print("   Good luck!")

def display_levels():
    """
    Display the levels of the game
    in the menu.
    """
    os.system('clear')
    print("Select a difficulty level:")
    # Define level items
    level_items = ["Easy - 20 tries, code length 4", "Medium - 10 tries, code length 4", "Hard - 10 tries, code length 5"]
    # Create a level menu object
    level_menu = TerminalMenu(level_items)
    # Show the level menu and get the user's selection
    level_entry_index = level_menu.show()

    # Handle user selection
    if level_entry_index == 0:
        return 20, 4
    elif level_entry_index == 1:
        return 10, 4
    elif level_entry_index == 2:
        return 10, 5

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
        display_rules()
        input("Press any key to return to menu.")
    elif menu_entry_index == 1:
        tries, code_length = display_levels()
        game(tries, code_length)
    elif menu_entry_index == 2:
        quit()

def generate_code(code_length):
    """
    Genereates a random code
    """
    code = [random.choice(COLORS) for _ in range(code_length)]
    return code


def guess_code(code_length):
    """
    Player / Users guess. 
    All code outputs need to look the same. 
    Can i add colors? 
    """
    guess = []
    for _ in range(code_length):
        # while loop until a valid color is provided
        while True:
            # Guess a color. The color number is the current loop index + 1
            color = input(f"Guess color {_ + 1}: ").upper()
            # If the guessed color is in the list of valid colors
            if color in COLORS:
                # Guessed color is added to the list
                guess.append(color)
                # Display the current state of the guess, with placeholders for the remaining colors
                # This is the magic!
                print(f"[ {' '.join(guess)}{' - ' * (code_length - len(guess))} ]")
                # Since a valid color has been guessed, exit the loop and move on to the next color
                break
            else:
                # ERROR on invalid color
                print(f"Invalid color: {color}. Try again. The valid colors are", *COLORS)
    return guess
    # Need a counter, you have {tries} left. Maybe. Maybe.

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

def game(tries, code_length):
    """
    HERE BE GAME!

    Doenst work...
    """
    os.system('clear')
    print(logo)
    print(f"Welcome to MasterMind. \nYou have {tries} tries to guess the code using {code_length} colors...")
    print("The valid colors are", *COLORS)

   # Generate the secret code
    real_code = generate_code(code_length)

    # Iterate through the allowed number of tries
    for attempts in range(1, tries + 1):
        # Get the player's guess
        guess = guess_code(code_length)

        # Check the guess against the real code
        check_code(guess, real_code)

        # Check if the guess is correct
        if sorted(guess) == sorted(real_code):
            os.system('clear')
            print(win)
            print(f"You guessed the code in {attempts} tries!\n A real MasterMind")
            break
    
    # If the player runs out of tries, display the correct code
    else:
        os.system('clear')
        print("You ran out of tries, the code was", *real_code)


# Main entry point of the program and i think it runs! YEY. :)
if __name__ == "__main__":
    while True:
        main_menu()