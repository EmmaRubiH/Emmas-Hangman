# Emmas Hangman Game

Hangman is a Python terminal game, wich runs in the Code Institue mock terminal on Heroku.

![Am I Responsive image](/assets/amiresponsive.png)

The Hangman game is about guessing letters (A-Z) to form the words. If the player guesses the right letter that is within the word,
the letter appears at its correct position. The user has to guess the correct word until a man is hung, then the game is over.
It has 3 python files, run.py, word.py and hangman_structure.py

The live link can be found here [Emmas hangman](https://emmas-hangman.herokuapp.com/)

## Features

The game features a welcome message to the user. To start the game the user needs to enter their name. The name must be letters only, if the user puts number an error message will appear. says "Username must be alphabets only".

![welcome image](/assets/welcome.png)

## Testing
* Tested for various bugs and functionality.
* tested for all scenarios with invalid guesses.
* Tested fpr all scenarios with successfull guesses.
* This game where only tested in crome, safari and firefox on a mac laptop divece.

### Validation testing
* Since the Pep8Online website is not working properly right now. 
I added the pep8 validation into my gitpod workspace directly.
* All errors and warnings were fixed, except for 'ms-toolsai.jupyter'. These will not affect the game, so i chose to leave them as they are. you can se them below.
![validation image](/assets/Validation.png)

## Bugs
1. Problems to get exit to work. after google alot i found out that i needed to import sys to get it to work.
2. I wanted to get to play again to work. that a user could type y and n if they wanted to continue playing. I was stuck for quite a while with how it would work. the problem was that I kept insisting that it would be functions within functions (). But then realized that I have to wrap all functions in one function to get it to loop.
## Deploymnet

### Heroku

1. Fork or clone this repository.
2. requirements.txt can be left empty as this project does not use any external libraries.
3. Create a new app in Heroku.
4. Select "New" and "Create new app".
5. Name the new app and click "Create new App".
6. In "settings" select "BuildPack" and select Python and Node.js.
7. While still in "settings", click "reveal Config Vars" and input the following KEY: PORT,VALUE:8000.
8. Click on "Deploy" an select your deploy method and repository.
9. Click "Connect" on selected repository.
10. Choose "Deploy Branch" in the manual deploy section.
11. You can choose "Enable Automatic Deploys" if you want.
12. Heroku will now deploy the site.

## Languages and technologies used

* Python
* Github
* Git
* Gitpod
* Heroku

## Credits

* For tutorial on hangman [Kylie Ying](https://youtu.be/cJJTnI22IF8)
* For tutorial on hangman [Tech with Mike](https://youtu.be/Ff--def_1q0)
* Extra help with if/else [Stackoverflow](https://stackoverflow.com/)
* welcome text idees [tds](https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b)
* How to play hangman[It sorcecode](https://itsourcecode.com/free-projects/python-projects/hangman-game-in-python-with-source-code/)