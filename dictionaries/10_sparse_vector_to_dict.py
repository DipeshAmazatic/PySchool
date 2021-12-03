# A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0, 0, 0, 0, 2, 0]. 
# Storing all those zeros wastes memory and dictionaries are commonly used to keep track of just the nonzero 
# entries. For example, the vector shown earlier can be represented as {0:1, 7:2}, since the vector it is meant 
# to represent has the value 1 at index 0 and the value 2 at index 7. Write a function that converts a sparse 
# vector into a dictionary as described above.


def convertVector(numbers):
    convert_vector={}
    for index,val in enumerate(numbers):
        if(val!=0):
            convert_vector[index]=val
    return convert_vector

print(convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]))
print(convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0]))
print(convertVector([0, 0, 0, 0, 0]))