# Write a recursive function numbersInbetween(start, end) that takes in two numbers and returns a common-separated 
# string with all the numbers in between the start and end number inclusive of both numbers.

def numbersInbetween(a, b):
    if(a>b):
        return "Invalid"
    if a == b:
        return str(a)
    else:
        return str(a)+','+numbersInbetween(a+1,b)


print(numbersInbetween(5, 10))
print(numbersInbetween(5, 0))
print(numbersInbetween(5, 5))
print(numbersInbetween(5, 8))