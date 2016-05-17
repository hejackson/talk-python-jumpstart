#!/usr/bin/local/python3
import random

print('----------------------------------------')
print('     GUESS THAT NUBMER GAME')
print('----------------------------------------')

the_number = random.randint(0,100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess == the_number:
        print('Correct {}, you won.  The number was {}'.format(name, guess))
    elif guess > the_number:
        print('{1}, your guess of {0} is too HIGH.'.format(guess, name))
    else:
        print('{}, your guess of {} is too LOW. '.format(name, guess))

