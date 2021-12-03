"""Define a function that takes in 3 values and determine if they can form the sides of an triangle."""
def isTriangle(x,y,z):
    if(x+y>z and y+z>x and z+x>y):
        return True
    return False
print(isTriangle(3,4,5))
print(isTriangle(1,3,1))