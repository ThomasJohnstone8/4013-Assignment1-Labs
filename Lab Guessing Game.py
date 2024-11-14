
"""

# Guessing game and welcome message
print("Welcome to the guessing game. A random number will be selected at the start between 1 and 100.")
print("You need to make a guess to what the number wll be.")
print("The program will tell you whether to guess higher or lower.")
print("Good luck!")

# Importing random number library
import random

random_number = random.randrange(1, 100)

# Enter the guess between 1 and 100
guess = int(input("Enter a number between 1 and 100: "))


while random_number != guess:

    if guess < random_number:  # Guess is too low
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > random_number:  # Guess is too high
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("You guessed correct! Thank you for playing my guessing game.")  # Wining message

"""

# Guessing game and welcome message
print("Welcome to the guessing game. A random number will be selected at the start between 1 and 100.")
print("You need to make a guess to what the number wll be.")
print("The program will tell you whether to guess higher or lower.")
print("The program will also limit your guesses to 10")
print("Good luck!")

# Importing random number
import random

# Making variables
randomNumber = random.randint(1, 100)
guess = ""
guessCount = 0
guessLimit = 10
outOfGuesses = False

# Main loop
while guess != randomNumber and not (outOfGuesses):
    if guessCount < guessLimit:
        guess = int(input("Enter your guess: "))
        guessCount += 1
        # Hint if the number is too high
        if guess > randomNumber:
            print("Too High, Guess Lower!")
            print(f"You have {guessLimit - guessCount} left!")
        # Hint if the number is too low
        elif guess < randomNumber:
            print("Too Low, Guess Higher!")
            print(f"You have {guessLimit - guessCount} left!")
    else:
        outOfGuesses = True

# If you run out of guesses the program will finish
if outOfGuesses:
    print("Out of guesses, Better luck next time!")
    print(f"The number was {randomNumber}")
    print(f"It took you {guessCount} to solve the number!")
else:
    print("You win, Thanks for playing!")
    print(f"It took you {guessCount} to solve the number!") # Winning message

