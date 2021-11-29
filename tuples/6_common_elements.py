# Write a function commonElements(t1, t2) that takes in 2 tuples as arguments and returns a sorted tuple
#  containing elements that are found in both tuples.

def commonElements(t1,t2):
    result=[]
    if(len(t1)>len(t2)):
        for i in t1:
            if(i in t2):
                result.append(i)
    else:
        for i in t2:
            if(i in t1):
                result.append(i)
    return tuple(result)


print(commonElements((1, 2, 3), (2, 5, 1)))
print(commonElements((1, 2, 3, 'p', 'n'), (2, 5 ,1, 'p')))
print(commonElements((1, 3, 'p', 'n'), ('a', 2 , 5, 1, 'p')))