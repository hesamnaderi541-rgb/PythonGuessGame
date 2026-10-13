
import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Try a higher number!")
    elif guess > secret_number:
        print("Try a lower number!")
    else:
        print("Congratulations! You guessed the number!")
        print("Number of attempts:", attempts)
        break
