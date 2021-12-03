# Write a function sortByIndex(aList) that takes in a list of tuple in the following format: (index, value) 
# and returns a new tuple with its elements sorted based on the index.

def sortByIndex(l1):
    le=len(l1)
    result=[]
    result.extend([' ']*le)
    for i in l1:
        result[i[0]-1]=i[1]
    return tuple(result)


print(sortByIndex([(4,'Python'), (1, 'Welcome'), (3, 'Begin'), (2, 'To')]))
print(sortByIndex([(2,'Programming'), (3, 'is'), (1, 'Python'), (4, 'Fun')]))
print(sortByIndex([(2,'is'), (3, 'Immutable'), (1, 'Tuple')]))