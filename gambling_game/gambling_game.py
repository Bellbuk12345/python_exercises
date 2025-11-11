
# Program: Simple Guessing / Gambling Game
# Description:
#   The system selects a random number between 1 and 5.
#   The user tries to guess the number.

#   If the user guesses correctly:
#       - Award: Free month of training
#   If the user guesses incorrectly:
#       - Penalty: Additional 600k payment for mentorship


import random

# Ask for user's name (used in result messages)
user_name = input("Enter your name: ")

def random_number_game():
    # Generate the system's secret number once
    system_number = random.randint(1, 5)

    while True:
        # Get user guess
        user_number = int(input("Enter a number between 1 and 5: "))

        # Validate input range
        if user_number < 1 or user_number > 5:
            print("Oops, enter a valid number between 1 and 5.")
            continue

        # Compare guess to system number
        if user_number == system_number:
            print(f"Oh wow! {user_name}, you've just earned yourself a FREE month of training!")
        else:
            print(f"Oops {user_name}, you must pay an additional 600k for your current mentorship.")

        # End the game after one valid guess
        break

    # Return the system number for reference/printing
    return system_number


# Call the function
system_number = random_number_game()

# Reveal system number at the end
print(f"The actual selected number was: {system_number}")

