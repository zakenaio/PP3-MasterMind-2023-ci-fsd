from art import logo, win
import random
print(logo)

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 5
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    print(code)
    return code

def game():
    generate_code()
    

game()