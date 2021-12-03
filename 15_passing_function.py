"""In Python, it is possible to pass a function as a argument to another
function. Write a function useFunction(func, num) that takes in a function
and a number as arguments. The useFunction should produce the output shown in the
examples given below."""

def addOne(x):
        return x + 1
        
def useFunction(func, num):
    return num**2

print(useFunction(addOne, 4))
print(useFunction(addOne, 9))
print(useFunction(addOne, 0))