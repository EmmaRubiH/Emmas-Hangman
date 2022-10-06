# Emmas Hangman Game

Hangman is a Python terminal game, wich runs in the Code Institue mock terminal on Heroku.

Users guess the right word by entering the right letters.
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

## Credits

* For tutorial on hangman [Kylie Ying](https://youtu.be/cJJTnI22IF8)
* For tutorial on hangman [Tech with Mike](https://youtu.be/Ff--def_1q0)
* Extra help with if/else [Stackoverflow](https://stackoverflow.com/)
* welcome text idees [tds](https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b)