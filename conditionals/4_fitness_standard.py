"""Define a function to determine the standard achieved by a participant taking a physical fitness test."""
def Fitness(a, b, c):
    if(a+b+c>=13 and a>3 and b>3 and c>3):
        return 'Gold'
    elif(a+b+c>=10 and a+b+c<13)and(a>2 and b>2 and c>2):
        return 'Silver'
    elif(a+b+c>=7 and a+b+c<10)and (a>1 and b>1 and c>1):
        return 'Pass'
    else:
        return 'Fail'
print(Fitness(4,5,4))
print(Fitness(4,4,4))
print(Fitness(1,5,5))
print(Fitness(2,2,5))