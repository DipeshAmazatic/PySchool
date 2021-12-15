"""Create a function addNumbers(num) that takes in a positive number as argument 
and returns the sum of all the number between 0 and that number (inclusive)."""

def addNumbers(num):
    sum_=0
    for i in range(1,num+1):
        sum_+=i
    return sum_
print(addNumbers(5))
print(addNumbers(0))