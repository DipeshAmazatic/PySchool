"""Create a function generateNumbers(start, end, step) that takes in three numbers 
as arguments and returns a list of numbers ranging from start to the end number 
(inclusive)and skipping numbers based on the step specified in the arguments.
 Note: The function range(x, y, z) can takes in 3 arguments. For example, 
 range(1, 11, 2) will return a list of numbers [1,3,5,7,9].
"""

def generateNumber(start,end_,step):
    return [i for i in range(start,end_+1,step)]

print(generateNumber(2, 10, 2))
print(generateNumber(10, 10, 1))
print(generateNumber(20, 0, -3))