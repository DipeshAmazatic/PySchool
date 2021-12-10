# Write a function getEvenNumbers(numbers) to return all the even numbers in a list.

def getEvenNumbers(numbers):
    return [i for i in numbers if(i%2==0)]


print(getEvenNumbers([1, 4, 8, 9]))
print(getEvenNumbers(range(1, 20, 3)))
print(getEvenNumbers([]))