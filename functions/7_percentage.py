"""Write a function percent(value, total) that takes in two numbers as
arguments, and returns the percentage value as an integer."""
def percent(value, total):
    return value * (total/100)

print(percent(46, 90))
print(percent(51, 51))
print(percent(63, 12))