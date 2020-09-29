'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
# Collaborators: Jonah, Bert, and Megan.

import random


def function(y,x):
    guesses = 0
    try:
        while True:

            if y == ('break'):
                break

            if guesses == 5:
                print("You are out of guess.")
                break

            if int(y) == x:
                print("You got the right answer!")
                break

            elif int(y) < x:
                print("Your number was too low, pick higher!")
                guesses = guesses + 1
                y = (input("Enter a number to guess or enter break to stop."))

            elif int(y) > x:
                print("Your number was too high, pick lower!")
                guesses = guesses + 1
                y = (input("Enter a number to guess or enter break to stop."))
    except:
         y = (input("Enter a number to guess or enter break to stop."))
         function(y,x)


a = int(input("Enter the first number of your guessing range:"))
b = int(input("Enter the second number of your guessing range:"))
y = input("Enter a number to guess or enter break to stop.")
x = random.randint(a,b)
function(y,x)

f = input("You are out of Guesses, enter 'again' to play again.")
if f == ("no"):
    quit()
elif f == ("again"):
    print("Here we go again")
    y = (input("Enter a number to guess or enter break to stop."))
    function(y,x)


