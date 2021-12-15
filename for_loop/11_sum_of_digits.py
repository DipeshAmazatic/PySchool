"""Write a function sumOfDigit(number) that takes in a number as argument 
and returns the sum of the individual digit in the number."""

def sumOfDigit(number):
    sum_=0
    for i in str(number):
        sum_+=int(i)
    return sum_
print(sumOfDigit(123))
print(sumOfDigit(234))
print(sumOfDigit(1000))
print(sumOfDigit(1001))