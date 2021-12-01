# abs(x) Return the absolute value of a number or the magnitude of a complex number.

# Write a function that returns the output as shown in the above examples.
def diff(a, b):
    if(type(a)==int):
        return a+b
    return abs(abs(a)-b) 

print(diff(3+4j,6))
print(diff(-5, 6))