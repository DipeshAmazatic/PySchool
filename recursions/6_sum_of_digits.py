# Write a recursive function sumOfDigits that takes in an integer and returns the sum of the digit in the integer.

def sumOfDigits(num):
    if(num==0):
        return 0
    return num%10+sumOfDigits(num//10)


print(sumOfDigits(1234))
print(sumOfDigits(4321))
print(sumOfDigits(111))
print(sumOfDigits(0))