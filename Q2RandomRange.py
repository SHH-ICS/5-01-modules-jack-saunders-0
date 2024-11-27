# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
# Q2RandomRange.py

import random

# Accepting two numbers as range limits
low = int(input("Enter the lower limit of the range: "))
high = int(input("Enter the upper limit of the range: "))

# Generate a random number within the specified range
random_number = random.randint(low, high)

# Display the result
print(f"A random number between {low} and {high} is: {random_number}")

