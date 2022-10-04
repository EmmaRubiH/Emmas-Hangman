import random
from hangman_structure import parts
from word import words

def welcome_user():
    """
    This function
    """
    username = None

    while True:
        username = input('Enter your name\n')

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
    It will
    """
    for letter in correct_guess:
        print(letter, end="")
    print()


def all_letter_only():
    """
    this function
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
    user_input = all_letter_only()
    if user_input in random_word:
        INDEX = 0
        for i in random_word:
            if i == user_input:
                correct_guess[INDEX] = user_input
            INDEX += 1
        update_correct_guess_list()

    else:
        if user_input not in correct_guess:
            incorrect_guess.append(user_input)
            parts(len(incorrect_guess))
            print(f'sorry, letter {user_input} is not in the word')

        else:
            print("You already guessed it, please try again...")
        print(incorrect_guess)
    
    if len(incorrect_guess) > 5:
        print("You lose, please try again")
        print("correct word is ", random_word)
        break

    if "_" not in correct_guess:
        print("Congratulations!!!, you have guessed the correct letter")
        break