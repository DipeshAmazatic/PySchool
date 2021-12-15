"""Create a function generateNumbers(num) that takes in a positive number as
argument and returns a list of number from 0 to that number inclusive. 
Note: The function range(5) will return a list of number [0, 1, 2, 3, 4]."""

def generateNumber(num): 
    return [i for i in range(num+1)]
print(generateNumber(1))
print(generateNumber(10))
print(generateNumber(0))