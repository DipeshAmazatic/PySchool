"""The Pythagoras' Theorem for a right-angle triangle can be written as
a2+b2 = c2, where a and b are sides of the right angle and c is the hypotenuse.
Write a function to compute the hypotenuse given sides a and b of the triangle.
"""
# Hint: You can use math.sqrt(x) to compute the square root of x.
import math
def hypotenuse(a, b):
    return int(math.sqrt(a**2+b**2))

print(hypotenuse(3, 4))
print(hypotenuse(5, 12))