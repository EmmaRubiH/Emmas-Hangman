import random

words = ['python', 'program']

picked = random.choice(words)

print('The word has', len(picked), 'letters')


right = ['_'] * len(picked)
wrong = []

def update():
    for i in right:
        print(i, end = ' ')
    print()

update()    

while True: 

    print('==================')

    guess = input("Guess a letter")

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index += 1

        update()

    else:
        if guess not in wrong:
            wrong.append(guess)
        else:
            print('You already guessed that')
        print(wrong)
    if len(wrong) > 4:
        print('You lose')
        print('I picked', picked)
        break
    if '_' not in right:
        print('You win')
        break