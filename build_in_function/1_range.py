# range([start,] stop[, step]) Function to create lists containing arithmetic progressions. 
# start is zero if omitted. step has a default value of 1 and must be non-zero. If step is positive, 
# the upper limit is stop-1. If step is negative, the lower limit is stop+1.

# Write a function that returns 4 lists given a postive number.
def createLists(num):
    return [list(range(1,num+1)),list(range(1,num+1))[::-1],[i*-1 for i in list(range(1,num+1))],[i*-1 for i in list(range(1,num+1))][::-1]]


print(createLists(5))