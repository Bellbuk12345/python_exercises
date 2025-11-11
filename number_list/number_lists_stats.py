
#Program: Number List Statistics
# File Name: number_list_stats.py

# Description:
#   This program prompts the user to enter 5 numbers, stores them
#   in a list, and then prints the sum, maximum, and minimum
#   values from the list.

# Concepts Covered:
#   - Lists
#   - For Loops
#   - User Input
#   - Built-in Functions (sum, max, min)


total_number = 0
added_number = [] # list to store user input

for user_number in range(5):

    user_number = int(input("Enter a number: "))
    added_number.append(user_number)
    total_number += user_number


print(f"The total sum of all the numbers entered is {total_number}")
print(f"The maximum number is:", max(added_number))
print(f"The minimum nmber is:", min(added_number))
