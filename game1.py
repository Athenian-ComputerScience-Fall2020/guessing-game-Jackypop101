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

x = random.randint(0,10)

def function():
    y = int(input("Choose a number."))

    if y == x:
        print("You got the right answer!")
    
    if y < x:
        print("Your number was too low, pick higher!")
        function()
    if y > x:
        print("Your number was too high, pick lower!")
        function()

function()


