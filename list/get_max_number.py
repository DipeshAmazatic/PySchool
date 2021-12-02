# Write a function getMaxNumber(numbers) that returns the maximum number in a list.

def getMaxNumber(numbers):
    if(numbers):
        return max(numbers)
    return 'N.A'

print(getMaxNumber([1, 4, 10]))
print(getMaxNumber(range(1, 20, 3)))
print(getMaxNumber([]))