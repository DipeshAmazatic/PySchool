#In Python, it is possible to pass a function as a argument to another 
# function. Write a function useFunction(func, num) that takes in a function 
# and a number as arguments.

def addOne(x):
        return x + 1
        
def useFunction(func, num):
    c=func(num)
    print(c**2)
useFunction(addOne,0)