import random

words = ['python', 'program']

picked = random.choice(words)


right = []
wrong = []

while True: 

    print('==================')

    guess = input("Guess a letter")


    if guess in picked:
        right.append(guess)
        print('Right:' ,right)
    else:
        wrong.append(guess)
        print('Wrong:' ,wrong)
