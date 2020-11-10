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


def function():
    #guesses that will go up every time you guess wrong.
    guesses = 0
    #asking for input of the range to guess in.
    a = int(input("Enter the first number of your guessing range:"))
    b = int(input("Enter the second number of your guessing range:"))
    y = input("Enter a number to guess or enter break to stop.")
    #Generating a random number for the player to guess.
    x = random.randint(a,b)
    #try and except function to allow the player to try again when they typed wrong.
    try:
        while True:
#by typing break they can stop playing.
            if y == ('break'):
                break
#Gives the player a total of 5 tries to guess the number,
            if guesses == 5:
                print("You are out of guess.")
                break
#if the number they guessed is equal to the random number, they won.
            if int(y) == x:
                print("You got the right answer!")
                break
#if the number they guessed is less than the random number, they need to guess higher
            elif int(y) < x:
                print("Your number was too low, pick higher!")
                guesses = guesses + 1
                y = (input("Enter a number to guess or enter break to stop."))
#if the number they guessed is lower than the random number, they need to guess lower.
            elif int(y) > x:
                print("Your number was too high, pick lower!")
                guesses = guesses + 1
                y = (input("Enter a number to guess or enter break to stop."))
#except function to help player type a number when they accidentaly typed something wrong.
    except:
         y = (input("Enter a number to guess or enter break to stop."))
         function()

#running the function
function()

#Allowing player to play again forever by running a while loop asking the player if they would like to play again every time they break out of the function.
while True: 
    f = input("You won! enter 'again' to play again.")
    #if no, game stops
    if f == ("no"):
        quit()
    #if yes, rerun the function
    elif f == ("again"):
        print("Here we go again")
        function()


