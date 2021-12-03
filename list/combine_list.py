# Write a function combineList(list1, list2) that takes in two lists as arguments and return a 
# list that combines all the elements in the two list.

def combineList(list1, list2):
    return list(list1)+list(list2)

print(combineList([1,2], [3, 4]))
print(combineList(range(5), range(5)))
print(combineList(range(5), ['a', 'b', 'c']))