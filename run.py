import random
from hangman_structure import parts
from word import words
from termcolor import colored


def welcome_user():
    """
    This function is for the user.
    They will input name with letters and not nummers.
    """
    print(
        colored("#######################################",
                'blue')
    )
    print(
        colored("     | H | A | N | G | M | A | N       ",
                'magenta')
    )
    print(
        colored("#######################################",
                'blue')
    )
    username = None

    while True:
        username = input('Enter your name to start\n')

        if not username.isalpha():
            print('Username must be alphabets only')
            continue
        else:
            print('Welcome '+username)
            break


print('Welcome to Hangman')
welcome_user()

random_word = random.choice(words)
print("Hint: The word has", len(random_word), "letters")
print("=================================")

correct_guess = ["_"] * len(random_word)
incorrect_guess = []


def update_correct_guess_list():
    """
    This function will print correct letters,
    in  to correct_guess
    """
    for letter in correct_guess:
        print(letter, end="")
    print()


def all_letter_only():
    """
    This function provide to only input letters
    not numbers
    """
    while True:
        user_input_letter = input("Type a letter: \n").lower()
        if not user_input_letter.isalpha():
            print('Error, please select a letter')
        else:
            return user_input_letter


update_correct_guess_list()
parts(len(incorrect_guess))


while True:
    print('==================')
    user_input = all_letter_only()
    if user_input in random_word:
        INDEX = 0
        for i in random_word:
            if i == user_input:
                correct_guess[INDEX] = user_input
            INDEX += 1
        update_correct_guess_list()

# For the wrong letter
    else:
        if user_input not in incorrect_guess:
            incorrect_guess.append(user_input)
            parts(len(incorrect_guess))
            print(
                colored(f"Oh no, letter {user_input} is not in the word",
                        'red')
                 )

        else:
            print(
                colored("You already guessed it, please try again...",
                        'blue')
                )
        print(incorrect_guess)
# this is for when the game ens with to many wrong letters.
# And shows the correct word that was choosen.
    if len(incorrect_guess) > 5:
        print(colored("Game is over, please try again", 'red'))
        print("correct word is ", random_word)
        break
# If all the letters to the word choosen is correct.
    if "_" not in correct_guess:
        print(
            colored("Congratulations!!!, you have guessed the correct letter",
                    'green')
            )
        break
