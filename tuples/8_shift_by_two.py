# Write a function shiftByTwo(*args) that takes in variable-length argument and returns a tuple with 
# its elements shifted to the right by two indices. See samples given below.

def shiftByTwo(*args):
    return args[len(args)-2:]+args[:len(args)-2]


print(shiftByTwo(1,2,3,4,5,6))
print(shiftByTwo('a','b','c','d'))
print(shiftByTwo('a','b'))
print(shiftByTwo('b'))