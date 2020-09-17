'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
# Collaborators: Jonah helped me a little bit by checking my code 

import random

x = random.randint(1,10)

def function():
    guesses = 0
    try:
        y = (input("Choose a number or press q to quit."))

        if y == (q):
            quit

        if int(y) == x:
            print("You got the right answer!")
    
        if int(y) < x:
            print("Your number was too low, pick higher!")
            guesses = guesses + 1
            function()
        if int(y) > x:
            print("Your number was too high, pick lower!")
            guesses = guesses + 1
            function()

        if guesses == 5:
            print("You are out of Guesses.")
    except:
        print("Please put in a number from 1-10")
        function()
    

function()


