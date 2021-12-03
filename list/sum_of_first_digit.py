# Write a function getSumOfFirstDigit(numList) that takes in a list of positive numbers and 
# returns the sum of all the first digit in the list.

def getSumOfFirstDigit(num):
    return sum([int(str(i)[0]) for i in num])

print(getSumOfFirstDigit([12, 23, 34, 45, 56]))
print(getSumOfFirstDigit([1, 23, 456, 7890]))
print(getSumOfFirstDigit([]))