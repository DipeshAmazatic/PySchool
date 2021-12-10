# sorted(iterable[, cmp[, key[, reverse]]]) Return a new sorted list from the elements in iterable.
# The key is a function that specifies the item in an element to be used for comparision.
# reverse sorts the elements in the opposite order.

# Write a function that sorts a list of questions that are organized by 's'tage and
# 'q'uestion numbers.
def cmpqn(a, b):
    if len(a)>len(b):
        return 1
    elif len(a)<len(b):
        return -1
    else:
        return 0

def sortqns(qnlist):
    return sorted(qnlist,key=cmpqn) 


print(sortqns(['s1q1', 's10q1', 's1q2', 's10q10', 's10q2']))