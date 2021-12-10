# Write a function addNumbersInList(numbers) to add all the numbers in a list. To access each element in a list, 
# you can use the statement 'for num in numbers:'.

def addNumbersInList(numbers):
    print(sum(numbers))

addNumbersInList([])
addNumbersInList([10, 20, 30])
addNumbersInList([-10, -20, 30])