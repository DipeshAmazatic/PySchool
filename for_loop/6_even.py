"""Create a function addEvenNumbers(start, end) that takes in two positive numbers
 as arguments and returns the sum of all the even numbers between the start and 
 end number (inclusive). Note: x % 2 returns 0 if x is an even number."""


def addEvenNumbers(start,end_):
    even_sum=0
    for i in range(start,end_+1):
        if(i%2==0):
            even_sum+=i
    return even_sum


print(addEvenNumbers(3, 7))
print(addEvenNumbers(5, 12))