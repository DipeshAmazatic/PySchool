"""Define a function isEven(number) that takes in a number as an argument
and returns True if it is an even number."""
def isEven(x): 
    if(x%2==0):
        return True
    return False
print(isEven(0))
print(isEven(1))
print(isEven(-2))