MasterMind

Initialt idea by Tech with Tim (LINK -  https://www.youtube.com/watch?v=sP-gFDreaQ4&themeRefresh=1)

My GitHub - 
My Live Deploy - 

I loved playing MasterMind when I was younger, I was never any good at it, but played it a lot. 
When I found Tech with Tims version it was a perfect plattform to build upon. 
Alterations. 
The idea is to break a 4 (or more) colored code in as few tries as possible. 


The user should be greeted with a Welcome message. print_welcome_message()
Logo and Menu. Start Game > levels - Rules - Quit. -Simple_term_menu. 
	
Need to Clear the Screen on Start / Quit, and menu options. 

The user Need visual feed back on their color choices and where they have placed them. 
For easiest use, choose one color at the time. Report errors if not a Color has been chosen. 
(You need to choose a color - Options RGBYWO
[ R G B Y ] 

Levels? 
Easy - Four colors 20 tries
Medium - Four colors 10 ties 
Hard - Five color colors 10 tries


Welcome Logo Message - print_welcome_message()
TOOL - https://textkool.com/en/ascii-art-generator

                                                    
Extended Python Version

simple_term_menu - LINK - https://pypi.org/project/simple-term-menu/
TerminalMenu handles all of the menu options. 

Menu. main_menu()
		Start Game - Starts Game()
		Rules of Mastermind display_rules()- Get you to The rules of the game. 
					with a return option. / Start game? 
		Quit - quit() quits the game. 


CLEAR SCREEN
import os
os.system('cls') # windows
os.system('clear')  # on linux / os x

COLORS R red G green B blue Y yellow W white O orange 
Use colorama for colors? 


Rules screen. 

def display_rules():
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



## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`


Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
