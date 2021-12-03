# reduce(function, iterable[, initializer]) Apply function of two arguments cumulatively to the items of iterable, 
# reducing the iterable to a single value.


# Write a factorial function using the 'reduce' function
from functools import reduce
def factorial(num):
    start = 1
    return reduce(lambda x,y:x*y,range(1,num+1),start)


print(factorial(4))
print(factorial(1))