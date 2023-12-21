# Import necessary modules
import random
import os
from art import logo

#CONSTANTS 
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 5
CODE_LENGTH = 4

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

def play_again():
    while True:
        answer = input("Do you want to play again? (yes/no): ").lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def game():
    """
    HERE BE GAME!

    Need to add menus, here? or over?
    """
    while True:
        os.system('clear')
        print(logo)
        print(f"Welcome to MasterMind. \nYou have {TRIES} tries to guess the code using {CODE_LENGTH} colors...")
        print("The valid colors are", *COLORS)

        real_code = generate_code()
        for attempts in range(1, TRIES + 1):
            guess = guess_code()
            check_code(guess, real_code)

            if sorted(guess) == sorted(real_code):
                print(f"You guessed the code in {attempts} tries!\n A real MasterMind")
                break

        else:
            print("You ran out of tries, the code was", *real_code)

        if not play_again():
            break

if __name__ == "__main__":
    game()