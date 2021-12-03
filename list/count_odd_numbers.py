# Write a function countOddNumbers(numbers) to count the number of odd numbers in a list.

def countOddNumbers(numbers):
    count=0
    return len([i for i in numbers if(i%2==1)])

print(countOddNumbers([1, 4, 8, 9]))
print(countOddNumbers(range(1, 20, 3)))
print(countOddNumbers([]))