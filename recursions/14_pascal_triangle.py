# The Pascal's Triangle is formed by filling the top 2 rows with '1's. For subsequent row, the numbers at 
# the edge are all '1's. Each element inside the triangle is the sum of the 2 elements above it. Write a 
# recursive function to compute the value of each element given the row and column.

def pascal(row, col):
    if(row==0):
        return 1
    elif(row>4):
        return int(list(str(11**row))[col-1]+list(str(11**row))[col])
    else:
        return int(list(str(11**row))[col])


print(pascal(0, 0))
print(pascal(2, 0))
print(pascal(4, 2))
print(pascal(5, 1))