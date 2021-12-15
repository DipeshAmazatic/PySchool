"""Write a function getBiggerNumber(x, y) that takes in two numbers as
arguments and returns the bigger number."""
def getBiggerNumber(first,second):
    """bigger number"""
    if first > second:
        return first
    return second

print(getBiggerNumber(20, -10))
print(getBiggerNumber(10, -10))
print(getBiggerNumber(10, 20))