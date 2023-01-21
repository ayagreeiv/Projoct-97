
import random
print("Number Gussing game")
number = random.randint(1,10)
chances = 0
print("Guess a number (between 1,10)")

while chances < 5:

    guess = int(input("Place your guess"))

    if guess == number:
        print("YOU DID IT!")

    elif guess < number:
        print("Guess higher than" , guess)
    else :
        print("Guess lower than" , guess)

if not chances < 5:
    print("YOU LOSE!! The number is", number)