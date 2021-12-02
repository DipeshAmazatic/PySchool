# A mxn matrix, m rows and n columns, can be represented using nested lists. Write a function that 
# returns the diminensions of a matrix.

def matrixDimensions(m):
    for i in m:
        if(len(m[0])==len(i)):
            pass
        else:
            return "This is not a valid matrix."
    return "This is a {}x{} matrix.".format(len(m),len(m[0]))

a = [ [1, 3], [-5, 6], [2, 4]]
print(matrixDimensions(a))
b = [ [1, 3, 2], [-5, 6, 0] ]
print(matrixDimensions(b))
c = [ [1, 3], [-5, 6, 0] ]
print(matrixDimensions(c))