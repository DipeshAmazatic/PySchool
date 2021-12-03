# Write a function combine(la, lb) that takes in two lists and return a list with the 
# contents of both list sorted in ascending order.

def combine(la, lb):
    return sorted((list(la)+list(lb)))


print(combine(['a', 'p', 'l'], ['g','o','l']))
print(combine(range(10, 2, -2), range(1, 10, 3)))
#print(combine(['a', 1, 'z'], [2, 4, 'y']))