"""Define a function isPrime(number) that takes in a number as argument and return
True if the number is a prime number."""
# Hint: Step through the range between (2, number-1), 
# and determine if the number is divisible using the modulus operator.
def isPrime(x):
    if(x<=1):
        return False
    else:
        for i in range(2,(x//2)+1):
            if(x%i==0):
                return False
        return True
    
print(isPrime(97))
print(isPrime(1))
print(isPrime(-2))