#GUESSING NUMBERS GAME
#The purpose of this game is to have the player enter a number between 1-101. They have 25 tries to do so.
#I have imported from the random library to generate the correct number. The user is prompted to enter their
#number, and after every guess is told whether they need to guess higher, lower, or if they are correct. A print 
#statement is displayed if their guess is correct, and how many tries it took for them to accomplish that. 
#Ultimately, the point of this simple code is to test probability, to see if there is a science behind
#the random function, using a sample set of 101 (integers between 1-101). I will have the user play this 
#game 3 sets of 25 times to prove my hypothesis (that there is a method to guessing the correct number in 
#25 tries or under) true.

#import from random library
import random

#initialize variable 'guesses' to 0
guesses = 0

#setting the range of numbers for the player to guess from
#by calling randint function to store the restore value in variable 'num'
num = random.randint(1, 101)
#print statement to instruct user how to play the game
print("This is a Guessing Numbers Game. You have 25 tries to guess the correct number. Please enter a number between 1 - 101.")

#this while loop allows the user to guess a maximum of 10 times
#if their guess is too low, they will be advised to guess higher.
#if their guess is too high, they will be advised to guess lower.
#if their guess is correct, they will be told so and how many tries
#it took them. If after 10 tries, they still did not guess the correct 
#number, they are told that their guesses were wrong, and what the 
#correct number was. This is all executed through the following while 
#loop, if, and print statements.
while guesses < 25:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    
    guesses = guesses + 1

    if guess < num:
        print("Guess Higher.")

    if guess > num:
        print("Guess Lower.")

    if guess == num:
        break

#this if statement runs if the user guessed the correct number
#followed by a print statement that notifies the user that their
#guess was correct and how many tries they took to accomplish that.
if guess == num:
    guesses = str(guesses)
    print("You guessed the correct number in " + guesses + " tries.")

#this if statement runs if the user did not guess the correct number
#within 10 tries, and notifies them what the correct number was.
if guess != num:
    num = str(num)
    print("Wrong, the correct number was " + num)