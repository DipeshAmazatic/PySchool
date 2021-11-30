# Write a function createPattern(n) that takes in a number as argument and returns a string based on the following
#  rules. The middle character of the string should always be an asterisk ('*'). There will be 2 asterisks if 
# there is an even number of characters. The string will contain the less-than character ('<') before the asterisk
#  and the greater-than character ('>') after the asterisk.

def createPattern(x):
    if(x == 1):
        return '*'
    elif(x == 2):
        return '**'
    elif(x%2==0):
        return '<'*((x-1)//2)+'**'+'>'*((x-1)//2)
    else:
        return '<'*(x//2)+'*'+'>'*(x//2)


print(createPattern(1))
print(createPattern(2))
print(createPattern(3))
print(createPattern(4))
print(createPattern(5))