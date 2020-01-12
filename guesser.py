#This is a guess the number game.
#You would guess a number between 1 and 100.
import random

print("Hello this a guess the number game!\n")

print("What is your name?\n")

name = input("Please, enter your name: ")

print("Hello, " + str(name) + "! " + "I would guess a number from 1 to 100.\n")

print("Try to guess!\n")

secretNumber = random.randint(1, 100)


for i in range (1,10):
	try:
		guess = int(input("Please, enter your guess: "))
		if guess < secretNumber:
			print("Nope, your number is too low! Try a bigger nubmer!\n")
		elif guess > secretNumber:
			print("Nope, your number is too high! Try a smaller number!\n")
		else:
			break
	except ValueError:
		print("Please, enter only digit numbers.\n")
		

if guess == secretNumber:
	print("BUNGO!" + str(name) + "You did it! You guess my number! Which was " + str(secretNumber) + "\n")
	print("And you did it in a " + str(i) + " attempts!\n")
else:
	print("Nope..., " + str(name) + ". I was thinking about " + str(secretNumber) + "\n")
	print("Let's play one more time..")




