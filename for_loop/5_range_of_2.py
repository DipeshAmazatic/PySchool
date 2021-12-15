"""Create a function addNumbers(start, end) that takes in two positive numbers 
as arguments and returns the sum of all the number between the start and end number (inclusive)."""

def addNumbers(start,end_):
    sum_=0
    for i in range(start,end_+1):
        sum_+=i
    return sum_
print(addNumbers(3, 7))
print(addNumbers(5, 6))