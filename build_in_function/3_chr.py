# chr(i) Return a character whose ASCII code is the integer i. i is between 0 and 255 inclusive.

# Write a function that returns a string of characters based on a list of ASCII codes.
def toString(alist):
    result=''
    for i in alist:
        result+=chr(i)
    return result
print(toString([112, 121, 115, 99, 104, 111, 111, 108, 115]))