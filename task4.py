#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
import math
print("This is a program to find the hypotenuse of a right triangle with legs side1 and side2.")
side1=float(input("Enter a value for side1. "))
side2=float(input("Enter a value for side2. "))
hypsqrd=side1**2 + side2**2
hypotenuse=math.sqrt(hypsqrd)
print(hypotenuse)
