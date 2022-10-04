words = ['python', 'program']

picked = random.choice(words)

print('The word has', len(picked), 'letters')


right = ['_'] * len(picked)
wrong = []


def update():
    for i in right:
        print(i, end=' ')
    print()


print('Let me think of a word')


def wait():
    for i in range(5):
        print('.', end='')
        sleep(.5)
    print()

wait()

update()
parts(len(wrong))   

while True: 

    print('==================')

    guess = input("Guess a letter")
    print('Let me check')
    wait()

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
            parts(len(wrong))
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


    
