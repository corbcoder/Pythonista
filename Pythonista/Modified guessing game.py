# The challenge.3 Chp.3
# 08/07/2022
# The computer picks a random number between 1 and 100
# The player tries to guess it in 5 tries and the computer lets
# the player know if the guess is too high, too low
# or right on the money within the number of tries but if, scolds the player for poor attempts.

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 10 few attempts if you can.\n")

# Set the initial values

the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop

# Be careful with indentation, especially after them cos it can create infinite loops.

while guess != the_number:
    tries += 1
    if tries > 10:
        print("Ouch! You almost guessed it but you ran out of guessing steam, try next time.\n")
        break
    elif guess > the_number:
        print("Wow!, go lower..")
    else:
        print("Hmm, pls go higher..")

    guess = int(input("take a guess: "))
    if guess == the_number:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")



input("\n\nPress the enter key to exit.")


