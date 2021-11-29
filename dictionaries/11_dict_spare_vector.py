# A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0, 0, 0, 0, 2, 0]. Storing all
#  those zeros wastes memory and dictionaries are commonly used to keep track of just the nonzero entries. 
# For example, the vector shown earlier can be represented as {0:1, 7:2}, since the vector it is meant to 
# represent has the value 1 at index 0 and the value 2 at index 7. Write a function that converts a dictionary 
# back to its sparse vector representation.


def convertDictionary(dictionary):
    list1=[]
    if(list(dictionary.keys())):
        le=list(dictionary.keys())[-1]
        list1.extend([0]*(le+1))
        for i in dictionary:
            list1[i]=dictionary[i]
        return list1
    else:
        return list1

print(convertDictionary({0: 1, 3: 2, 7: 3, 12: 4}))
print(convertDictionary({0: 1, 2: 1, 4: 2, 6: 1, 9: 1}))
print(convertDictionary({}))