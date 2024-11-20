# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
# Q1Pythagoras.py

# Function to calculate the hypotenuse
def calculate_hypotenuse(a, b):
    # Calculate c (hypotenuse) using the Pythagorean theorem
    c = (a ** 2 + b ** 2) ** 0.5
    return c

# Input from the user for the two legs of the right-angled triangle
a = float(input("Enter the length of the first leg (a): "))
b = float(input("Enter the length of the second leg (b): "))

# Calculate the hypotenuse
c = calculate_hypotenuse(a, b)

# Output the result with labels
print(f"The length of the hypotenuse (c) is: {c:.2f}")
