# Write a function getNumbers(number) that takes in a number as argument and return a list 
# of numbers as shown in the samples given below.
def power(n):
    return n**2

def getNumbers(num):
    if(num%2==0):
        x=list(map(power,list(range(0,num+1,2))))
        return x[1:][::-1]+x
    else:
        x=list(map(power,list(range(1,num+1,2))))
        return x[0:][::-1]+x


print(getNumbers(10))
print(getNumbers(9))
print(getNumbers(0))