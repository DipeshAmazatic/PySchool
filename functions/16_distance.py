"""Write a function calDistance(x1, y1, x2, y2) to calculate the distance
between two points represented by Point 1 (x1, y1) and Point 2 (x2, y2).
The formula for calculating distance is given below:"""
import math
def calDistance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


print(calDistance(1, 0, 0, 0))
print(calDistance(1, 1, 1, 1))
print(calDistance(0, 0, 1, 1))