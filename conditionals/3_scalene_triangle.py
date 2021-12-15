"""Write a function isScalene(x, y, z) that accepts the 3 sides of a triangle
as inputs. The function should return True if it is a scalene triangle. A scalene
triangle has no equal sides."""

def isScalene(x, y, z):
    if(x==y or y==z or x==z):
        return False
    return True

print(isScalene(2, 4, 3))
print(isScalene(3, 3, 3))
print(isScalene(2, 2, 3))