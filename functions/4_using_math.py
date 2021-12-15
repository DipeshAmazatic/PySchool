"""Python provides many built-in modules with many useful functions.
One such module is the math module. The math module provides many useful
functions such as sqrt(x), pow(x, y), ceil(x), floor(x) etc. You will need to
do a "import math" before you are allowed to use the functions within
the math module."""

import math
# Calculate the square root of 16 and stores it in the variable a
A = math.sqrt(16)

# Calculate 3 to the power of 5 and stores it in the variable b
B = math.pow(3, 5)

# Calculate area of circle with radius = 3.0 by making use of the math.
# pi constant and store it in the variable c
C = math.pi * math.pow(3.0,2)
print(A,B,C)