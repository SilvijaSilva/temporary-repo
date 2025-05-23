print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 10")
print("Enter 'quit' to exit the game at any time.")

import random

parsed_guess = 0
number_to_guess = random.randint(1, 10)

while parsed_guess != number_to_guess:
    user_input = input("Please enter your guess: ")

    if user_input == "quit":
        print("Thanks, bye!")
        exit()

    print("You guessed: " + user_input)
    
    # print(f"You guessed: {user_input}")

    try:
        parsed_guess = int(user_input)
    except Exception:
        print("Invalid input. Please enter a number between 1 and 10.")
        exit()

    if parsed_guess < 1 or parsed_guess > 10:
        print("Invalid guess. Please enter a number between 1 and 10.")
    elif parsed_guess < number_to_guess:
        print("Too low!")
    elif parsed_guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed the correct number.")