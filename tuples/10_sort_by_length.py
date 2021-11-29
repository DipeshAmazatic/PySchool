# Write a function sortByLength(t, order) that takes in a tuple of string and returns a new tuple with its 
# elements sorted by the length of the string. The order of sorting is based on the value of 
# the second argument: 'asc' or 'des'.


def sortByLength(t,order):
    t=list(t)
    le=[]
    for i in t:
        le.append(len(i))
    result=[]
    l=len(le)
    for i in range(l):
        result.append(t[le.index(max(le))])
        
        t.remove(t[le.index(max(le))])
        le.remove(max(le))
    if(order=='asc'):
        return tuple(result[::-1])
    return tuple(result)


print(sortByLength(('iOS', 'iPhone', 'iPad'), 'asc'))
print(sortByLength(('apple', 'orange', 'pear'), 'des'))
print(sortByLength(('begin', 'python', 'programming'), 'des'))
print(sortByLength(('begin', 'python', 'programming'), 'asc'))