# Write a function removeCommonElements(t1, t2) that takes in 2 tuples as arguments and returns a sorted 
# tuple containing elements that are not found in both tuples.

def removeCommonElements(t1,t2):
    re=[]
    t2=list(t2)
    for i in t1:
        if(i not in t2):
            re.append(i)
        else:
            t2.remove(i)
    return tuple(re+t2)

print(removeCommonElements((1,2,3,4), (3,4,5,6)))
print(removeCommonElements(('b','a','c','d'), ('a','b','c')))
print(removeCommonElements(('a','b','c'), ('a','b','c')))
print(removeCommonElements(('a','b'), ('c', 'd')))
print(removeCommonElements(('b','a','d','c'), ('a','b')))