# Write a function invertDictionary(d) that takes in a dictionary as argument and return a dictionary 
# that inverts the keys and the values of the original dictionary.


def invertDictionary(d):
    invert_dict={}
    for i in d:
        if(d[i] in invert_dict):
            invert_dict[d[i]].append(i)
        else:
            invert_dict[d[i]]=list([i])
    return invert_dict



print(invertDictionary({'a':1, 'b':2, 'c':3, 'd':2}))
print(invertDictionary({'a':3, 'b':3, 'c':3}))
print(invertDictionary({'a':2, 'b':1, 'c':2, 'd':1}))