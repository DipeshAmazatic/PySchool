"""Define a function calls addFirstAndLast(x) that takes in a list of numbers
and returns the sum of the first and last numbers."""
def addFirstAndLast(x):
    if(x):
        return x[0]+x[len(x)-1]
    return 0

print(addFirstAndLast([]))
print(addFirstAndLast([2, 7, 3]))
print(addFirstAndLast([10]))