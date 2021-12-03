# Write a function printTwos(n) that takes in a number as argument and returns a string composed of an odd 
# number multiplied by 2s such that the final value is equal to n. There should be equal number of 2s on both sides. 
# Extra 2 should appear at the front of the string. Note: The value of the odd number can be 1.

def printTwos(n):
    if(n==1):
        return '1'
    elif(n%2==0):
        return '2'+' * '+printTwos(n//2)
    else:
        return str(n)


print(printTwos(1))
print(printTwos(2))
print(printTwos(10))
print(printTwos(20))
print(printTwos(30))
print(printTwos(32))
print(printTwos(80))
