#Exercise 4.10
"""(Guess the number) Write a scrpit that plays guess the number, do not tell the user the number until guessed.  Give the user feedback if they guessed the number"""
#Import random library
import random

#Define a function that runs the guessing game
def game():
    #Establish local variables
    guess = -1
    rand = random.randrange(0,21)
    #Create while loop that reads the user input and gives output on if the guess is high, low, or correct
    while guess != rand:
        guess = int (input('Guess a number between 0 and 20: '))
        if guess < rand:
            print('Too low! Try again!')
        elif guess > rand:
            print('Too High! Try again!')
        elif rand == guess:
            print('Congratulations! You guessed the number!')
        else:
            print('Error')

#Define a function that controls the number of times played
def play_game():
    while True:
        #Calls the games function
        game()
        #When game loop exits, prompts user if they want to play again
        choice = input ("Do you want to play again? (y/n)")
        #If no the function exits and the code ends
        if choice == 'n':
            break

#Runs the play_game function
play_game()