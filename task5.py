#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.
import math
print("This is a program to find the radius of a sphere when given volume.")
volume=float(input("Enter the volume of a sphere. "))
coeff=4/3
FirstStep=volume/coeff
cube=FirstStep/math.pi
exp=1/3
radius=cube**exp
print(radius)
