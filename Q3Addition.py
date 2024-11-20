# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
# Q3Addition.py

import random

# Function to generate two random numbers and ask an addition question
def ask_addition_question():
    # Generate two random numbers between 1 and 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    # Ask the user the addition question
    print(f"What is {num1} + {num2}?")
    
    # Input the user's answer
    user_answer = int(input("Your answer: "))
    
    # Calculate the correct answer
    correct_answer = num1 + num2
    
    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Correct! Well done.")
    else:
        print(f"Oops! The correct answer is {correct_answer}.")

# Run the function to ask the addition question
ask_addition_question()
