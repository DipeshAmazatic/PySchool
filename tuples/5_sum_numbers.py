# n python, it is possible to pass in variable-length argument to a function by using the following notation: 
# *args. The argument is passed in as a tuple.

# Write a function sumNumbers(*args) that takes in a variable-length argument list of numbers and returns the 
# sum of the numbers.


def sumNumbers(*args):
    return sum(args)


print(sumNumbers(1,2,3,4,5))
print(sumNumbers(1,2,3))
print(sumNumbers(1))