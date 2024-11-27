# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
# Q3Addition.py

import random

# Generate two random numbers between 1 and 100
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Ask the user to solve the addition question
answer = int(input(f"What is {num1} + {num2}? "))

# Check if the answer is correct
if answer == num1 + num2:
    print("Correct! Well done.")
else:
    print(f"Oops! The correct answer was {num1 + num2}.")
