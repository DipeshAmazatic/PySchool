"""The smallest common multiple of two or more numbers is called the lowest common
multiple (LCM). Given a list of integers, find the lowest common multiple."""

from functools import reduce
def lcm(x,y):
    tmp=x
    while (tmp%y)!=0:
        tmp+=x
    return tmp

def LCM(args):
    return reduce(lcm,args)
print(LCM([2, 3, 4]))
print(LCM([3, 6, 9]))
print(LCM([3, 3]))