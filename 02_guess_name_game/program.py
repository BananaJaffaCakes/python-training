import random

print('-----------------')
print('GUESS THAT NUMBER')
print('-----------------')

player_name = input('Enter your player name: ')

the_number = random.randint(1, 100)

print('A random number between 1 and 100 has been generated, can you guess the number {}?'.format(player_name))

guess = 0

while guess != the_number:
    player_guess = input('Enter your guess: ')
    guess = int(player_guess)
    if guess == the_number:
        print('Well done, the number was {}.'.format(the_number))
    elif guess > the_number:
        print('Sorry {0}, your guess of {1} was too HIGH, try again!'.format(player_name, guess))
    else:
        print('Sorry {0}, your guess of {1} was too LOW, try again!'.format(player_name, guess))

print('Thank you for playing {}, the game is now ending!'.format(player_name))