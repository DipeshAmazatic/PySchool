"""Write a function getSumOfLastDigits() that takes in a list of
positive numbers and returns the sum of all the last digits in the list."""

def getSumOfLastDigits(numList):
    sum_=0
    for i in numList:
        sum_+=int(str(i)[-1])
    return sum_
print(getSumOfLastDigits([2, 3, 4]))
print(getSumOfLastDigits([1, 23, 456]))