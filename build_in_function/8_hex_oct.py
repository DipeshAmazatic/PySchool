# hex(x) Convert an integer number to a hexadecimal string.
# oct(x) Convert an integer number to a octal string.

# Write a function that converts a decimal integer to both hexadecimal and octal format.
def dec2hexoct(x):
    return (hex(x),oct(x))


print(dec2hexoct(64))