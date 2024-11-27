# Q1Pythagoras.py

import math

# Accepting inputs from the user for the two legs of the triangle
a = float(input("Enter the length of the first leg of the right-angle triangle (a): "))
b = float(input("Enter the length of the second leg of the right-angle triangle (b): "))

# Calculate the length of the hypotenuse using the Pythagorean theorem
c = math.sqrt(a**2 + b**2)

# Display the result
print(f"The length of the hypotenuse (c) is: {c:.2f}")
