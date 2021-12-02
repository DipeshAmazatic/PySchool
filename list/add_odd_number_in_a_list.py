# Write a function addOddNumbers(numbers) to add all the odd numbers in a list. To access each element in a list, 
# you can use the statement 'for num in numbers:'.

def addOddNumbers(numbers):
    return sum([i for i in numbers if(i%2==1)])


print(addOddNumbers([1, 4, 8, 9]))
print(addOddNumbers(range(1, 20, 3)))
print(addOddNumbers([]))