# My first python program
# To help familiarize myself with python syntax

import random
secretNumber = random.randint(1, 20)
print(‘I am thinking of a number between 1 and 20.’)

# Gather user input up to 6 times
for guessesTaken in range(1, 7):
	print (‘Take a guess.’)
	guess = int(input())

	if guess < secretNumber:
		print(‘Your guess is too low’)
	elif guess > secretNumber:
		print(‘Your guess is too high.’)
	else:
		 break # user has guessed correctly

if guess == secretNumber:
	print('Congrats, you guess the correct number om ' +str(guessesTaken) + ' guesses!')
else:
	print('Sorry, the correct answer was ' +str(secretNumber))

