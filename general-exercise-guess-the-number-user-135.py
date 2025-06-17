"""
Exercise: Guess the Number (id=135)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if name == ‘main’:" block.

Requirements:
Write a Python program that generates a random number between 1 and 100 and asks the user to guess the number. The program should provide feedback to the user after each guess.

Instructions
Implement guess_the_number function according to the specified requirements. Use loops and conditional statements to generate a random number and ask the user to guess it. Provide feedback to the user after each guess. Return the number of guesses it took for the user to guess correctly.

Examples
Here is an example to illustrate the expected behavior of your function:

Input: guess_the_number() Output: "What is your guess? " 50 "You are wrong! You guessed the number in 1 guess. You guessed too high."

Input: guess_the_number() Output: "What is your guess? " 25 "You are wrong! You guessed the number in 2 guesses. You guessed too low."

Input: guess_the_number() Output: "What is your guess? " 37 "Congratulations! You guessed the number in 3 guesses."

Input: guess_the_number() Output: "What is your guess? " 101 "You are completely wrong! The number is between 1 and 100." 

Input: guess_the_number() Output: "What is your guess? " 0 "You are completely wrong! The number is between 1 and 100."

Input: guess_the_number() Output: "What is your guess? " "You are completely wrong! The number is between 1 and 100."


"""

import random

def guess_the_number():
    # Your code goes here

    #You need to generate a random number between 1 and 100.
number = random.randint(1, 100)

#you need to prompt the user to guess the number. You’ll want to make sure to capture their input and convert it to an integer.
guess = int(input("Guess the number between 1 and 100: "))

#You need to compare the user’s guess to the randomly generated number and give feedback.
if guess == number:
    print("Correct!")
else:
    print("Too high!")

#You want to repeat the guessing process until the user guesses the correct number.
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess == number:
        break

#You want to keep track of how many guesses it took for the user to guess the correct number.
guesses = 0
while guess != number:
    guess = int(input("Guess the number between 1 and 100: "))
    guesses += 1

#Finally, you want to provide feedback on how many guesses it took the user to get the correct number.
print(f"Correct! It took you {guesses} guesses.")

#out of range
if guess < 1 or guess > 100:  # Case for out of range guesses
    print("Please guess a number between 1 and 100.")
    continue



#------ whole code together --

import random

def guess_the_number():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    guesses = 0  # Initialize guess counter
    
    while True:
        # Get user input and handle invalid cases (empty, less than 1, or greater than 100)
        guess_input = input("Guess the number between 1 and 100: ")
        
        if not guess_input:  # Case for empty input
            print("Input cannot be empty. Please enter a number.")
            continue
        
        try:
            guess = int(guess_input)
        except ValueError:  # Case for non-integer input
            print("Invalid input! Please enter a valid number.")
            continue
        
        if guess < 1 or guess > 100:  # Case for out of range guesses
            print("Please guess a number between 1 and 100.")
            continue
        
        guesses += 1  # Increment guess counter
        
        # Provide feedback on the guess
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! It took you {guesses} guesses.")
            break  # Exit the loop when the guess is correct


    pass

if __name__ == '__main__':
    guess_the_number()