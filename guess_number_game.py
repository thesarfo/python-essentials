import random

print("Welcome to the guessing game! You have 7 tries and 3 hints.")
number = random.randint(1, 100)
guesses = 0
hints = 0

for i in range(7):
	guess = int(input("Guess a number between 1 and 100: "))
	guesses += 1
	
	if guess < number:
		print("Too low!")
	elif guess > number:
		print("Too high!")
	else:
		print("Congratulations, you guessed the number in", guesses, "guesses!")
		break
	
	if guesses == 4 and hints < 3:
		print("Hint: The number is between", number-10, "and", number+10)
		hints += 1

if guesses == 7:
	print("Sorry, you didn't guess the number. The number was", number)
