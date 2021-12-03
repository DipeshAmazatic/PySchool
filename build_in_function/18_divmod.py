# divmode(a, b) Return the quotient and remainder of a/b.
# For integers, result is the same as (a // b, a % b).

# Write a function that returns the exponent of a positive number given its base.
def exponent(num,base):
    exp = 0
    while(divmod(num,base)[0]):  # loop while the quotient is non-zero
        exp+=1
        num=divmod(num,base)[0]

    return exp 

print(exponent(8, 2))
print(exponent(25, 5))