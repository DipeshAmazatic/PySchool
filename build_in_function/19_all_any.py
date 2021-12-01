# all(iterable) Return True if all elements of the iterable are true.
# any(iterable) Return True if any element of the iterable is true. If the iterable is empty, return False.

# Write a function that checks if some or all of the items are true or false.
def checkItems(items): 
    if (all(items)):
        return "All are true"
    elif(any(items)):
        return "Some are true"
    else:
        return "All are false"

print(checkItems([1, 2, 3]))
print(checkItems([{'a':1}, 'hello', 0]))
print(checkItems([0, (), '']))