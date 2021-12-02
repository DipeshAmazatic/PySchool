# Write a function getMinNumber(numbers) that returns the minimum number in a list.

def getMinNumber(numbers):
    if(numbers):
        return min(numbers)
    return 'N.A'

print(getMinNumber([12, 4, 10]))
print(getMinNumber([]))