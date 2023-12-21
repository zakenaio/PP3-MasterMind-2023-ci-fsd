from art import logo, win
import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 20
CODE_LENGHT = 4

def generate_code():
    """
    Generates a random code by selecting a color 
    from the COLORS list for each position in the
    code and then returning the code.

    This need a rewrite. 
    
    """
    code = []
    for _ in range(CODE_LENGHT):
        color = random.choice(COLORS)
        code.append(color)
    print(code)
    return code


def guess_code():
    """
    Player / Users guess. 
    """
    # Prompt the user to input a guess and convert it to uppercase
    while True:
        guess = input("Guess: ").upper().split(" ")

        # Check if the length of the guess is not equal to the predefined code length
        if len(guess) != CODE_LENGHT:
            print(f"You must guess {CODE_LENGHT} colors.")
            continue

        # Check if each color in the guess is a valid color
        for color in guess:
            if color not in COLORS:
                print(f"Invalid colors: {color}. Try again.")
                break
        else:
            break
        
    return guess

def check_code(guess, real_code):
    """
    Checks code 'guess' against 'real_code' 
    USE ZIP! Go back to lovesandwich. 
    """
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    
    for guess_color, real_color in zip(guess, real_code):
        # The zip function combines the elements of guess and real_code into tuples for comparison
        if guess_color == real_color:
            # If color + possition is correct, add 1
            correct_pos += 1
            # remove one guess_color in the color_counts 
            color_counts[guess_color] -= 1
        
    
    print(f"Guess: {guess} | Correct: {correct_pos} ")



def game():
    
    print(logo)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGHT:
            print(f"You guessed the code in {attempts} tries!")
            break
    
    
    print(code)

game()