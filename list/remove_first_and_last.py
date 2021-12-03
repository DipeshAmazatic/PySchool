# Write a function removeFirstAndLast(list) that takes in a list as an argument and remove the first 
# and last elements from the list. The function will return a list with the remaining items.

def removeFirstAndLast(numbers):
    numbers=list(numbers)
    if(len(numbers)>=2):
        numbers.remove(numbers[0])
        numbers.remove(numbers[len(numbers)-1])
    elif(len(numbers)==1):
        numbers.remove(numbers[0])
    return numbers


print(removeFirstAndLast([1, 4]))
print(removeFirstAndLast(range(1, 20, 3)))
print(removeFirstAndLast([1]))