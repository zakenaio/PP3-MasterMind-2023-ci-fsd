from art import logo, win
import random
print(logo)

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 5
CODE_LENGTH = 4

def generate_code():
    """
    Generates a random code by selecting a color 
    from the COLORS list for each position in the
    code and then returning the code.
    
    """
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    print(code)
    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGHT:
            print(f"You must guess {CODE_LENGHT} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid colors: {color}. Try again.")
                break
        else:
            break

    return guess

def game():
    generate_code()
    guess_code()
    

game()