# Write a function (list1, list2) that takes in two lists as arguments and return a list that is the result 
# of removing elements from list1 that can be found in list2.

def subtractList(list1, list2):
    list1=list(list1)
    list2=list(list2)
    for i in list2:
        if(i in list1):
            list1.remove(i)
    return list1


print(subtractList(range(5), range(4)))
print(subtractList([1,2,3,4,5], [2, 4]))
print(subtractList (['a', 'b', 'c', 'd'], ['x', 'y', 'z']))
