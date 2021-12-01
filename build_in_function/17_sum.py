# sum([iterable[, start]) Return the total of the items in an iterable. start is the initial value, and is zero by default.

# Write a function that returns the total of two sequences.
def totalSum(a, b):
    sum1=0
    for i in list(a),list(b):
        sum1+=sum(i)
    return sum1
print(totalSum(range(10), range(5)))
print(totalSum([1, 2, 3], (3, 4)))
print(totalSum([1, 2, 3], {1:3, 2:4}))