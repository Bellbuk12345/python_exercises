
# Program: Factorial Determination
# File Name: factorial.py

# Description:
#   This program defines a function that calculates the factorial
#   of a positive integer. It then tests the function using the
#   values 3, 4, and 5, which should return 6, 24, and 120.

# Input:
#   - One positive integer
# Output:
#   - The factorial of the given input number




def factorial_number(number):
    total = 1
    for n in range(1, number + 1):
        total *= n
    return total


# Testing the function with 3, 4, and 5 as required:
print(f"Factorial of 3 = {factorial_number(3)}")   # Expected: 6
print(f"Factorial of 4 = {factorial_number(4)}")   # Expected: 24
print(f"Factorial of 5 = {factorial_number(5)}")   # Expected: 120
