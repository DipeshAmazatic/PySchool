# Tuple is like list, except that it is immutable. However, the elements in a tuple can be mutable.
# Which of the following operation on a tuple 't' is valid?

t=((1,2), [3,4])
a = ([1,1] ,3)
a[0][1] = 2
print(a)
