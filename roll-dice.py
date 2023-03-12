import random


#this function generates the dice figures
def roll_dice():
    return random.randint(1, 6)


roll = input("Do you want to roll the dice (y/n): ").lower()

#this loop repeats the dice rolling over again
while roll == "y":
    result = roll_dice()
    print("You rolled a", result)

    #ask if the user wants to roll again
    roll = input("Do you want to roll again (y/n): y")

print("Thanks for playing")


