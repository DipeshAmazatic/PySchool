"""Write a function isEquilateral(x, y, z) that accepts the 3 sides of a
triangle as arguments. The program should return True if it is
an equilateral triangle."""

def isEquilateral(x, y, z):
    if x<0 or y<0 or z<0:
        return False
    elif(x==y and x==z and y==z):
        return True
    else:
        return False
print(isEquilateral(2, 4, 3))
print(isEquilateral(3, 3, 3))
print(isEquilateral(-3, -3, -3))