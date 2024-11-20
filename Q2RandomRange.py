# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
# Q2RandomRange.py

import random

# Function to generate a random number within a given range
def generate_random_number(start, end):
    return random.randint(start, end)

# Input from the user for the two numbers (range)
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Ensure the start is less than or equal to the end
if start > end:
    print("The starting number must be less than or equal to the ending number.")
else:
    # Generate and output a random number between the two numbers (inclusive)
    random_number = generate_random_number(start, end)
    print(f"A random number between {start} and {end} is: {random_number}")
