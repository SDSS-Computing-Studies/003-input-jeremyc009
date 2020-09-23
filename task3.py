#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
import math
print("This is a program to solve for x in equations of the form ax+b=c")
a=float(input("Input a value for a "))
b=float(input("Input a value for b "))
c=float(input("Input a value for c "))
FirstStep=c-b
x=FirstStep/a
print(x)
