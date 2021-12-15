"""Write a function isIsosceles(x, y, z) that accepts the 3 sides of a triangle as
inputs. The function should return True if it is an isosceles triangle. An
isosceles triangle has 2 equal sides. An equilateral triangle is a special case of
isosceles triangle."""

def isIsosceles(x, y, z):
    if(x<0 or y<0 or z<0):
        return False
    elif(x==y and x!=0) or (y==z and y!=0) or (z==x and z!=0) or (x==y and x==z and y==x and x!=0):
        return True
    return False

print(isIsosceles(2, 4, 3))
print(isIsosceles(3, 3, 3))
print(isIsosceles(2, 3, 2))
print(isIsosceles(-2, 3, -2))
print(isIsosceles(0, 0, 2))