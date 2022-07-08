# The challenge.1 Chp.3
# 08/07/2022
# Write a program that simulates a fortune cookie.
# The program should display one of five unique fortunes, at random, each time it’s run.

# Problem definition
# Program to generate different "fortune cookie" - quotes/sayings - to humor, every time it runs.
# Purpose
# Demonstrate the program ability to create random quotes within 5 runs (fun)
# Everytime program runs, you get a random quote out of five quotes.


import random

fortune_cookie = random.randint(1, 5)

if fortune_cookie == 1:
    print("Love, because it is the only true adventure.")
if fortune_cookie == 2:
    print("You’re intoxicating when you do what you love.")
if fortune_cookie == 3:
    print("Follow what you love and see what turns up.")
if fortune_cookie == 4:
    print("Focus on the magic of things; yourself.")
if fortune_cookie == 5:
    print("Change comes with embracing the future, not fighting your past.")
input("\nPress the enter key to exit.")
