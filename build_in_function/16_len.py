# len(s) Return the length (the number of items) of a sequnce (string, tuple or list) or a mapping (dictionary).

# Write a function that returns the total size of the arguments.
# Note: *args denotes a variable argument list, represented by a tuple.
def totSize(*args):
    len1=0
    for i in args:
        len1+=len(i)
    return len1

print(totSize('abc', (1,), [1,2,3]))