MasterMind

Initialt idea by Tech with Tim (LINK -  https://www.youtube.com/watch?v=sP-gFDreaQ4&themeRefresh=1)

My GitHub - https://github.com/zakenaio/PP3-MasterMind-2023-ci-fsd
My Live Deploy - https://mastermind2023-c32719b252cc.herokuapp.com/

I loved playing MasterMind when I was younger, I was never any good at it, but played it a lot. 
I did Tims version in early summer 2023, and had a lot of ideas of how to improve. 

The player should be greeted by a big friendly Logo. 
MasterMind 
And a menu for easy access to Rules, a way to choose levels, and to quit the game. 
The rules (found here) are really not that hard, but they are extensive
enough to cover a large part of the game screen. 
Not optimal. This was more or less the only reason for the menus. 

I really wanted levels, i would recquire a major overhaul of the games logic. 
Here the user is greeted by three different options. 

- Easy - Four colors 20 tries
- Medium - Four colors 10 ties 
- Hard - Five color colors 10 tries

The real challange for me was to make this work. Both game mechanics, and menus.
The user needs a seamless way to work. Easy up down and enter.

Single letter input with visual markers for where you have put your color. 
Here is yet another really important part of the new ux, its much easier
for the user to just input one color at the time, with visual feedback.
Instead of all four / or five for hard. 

[ R - - - ] 
[ R G - - ] 



Welcome Logo Message - print_welcome_message()
TOOL - https://textkool.com/en/ascii-art-generator


simple_term_menu - LINK - https://pypi.org/project/simple-term-menu/
TerminalMenu handles all of the menu options. 

Colorama LINK - https://pypi.org/project/colorama/

Menu. main_menu()



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
