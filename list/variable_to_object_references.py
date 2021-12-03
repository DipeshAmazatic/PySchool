# In Python, variables are linked to objects by references.
a = [4, 5, 6 ]
b = a
b[0] = 1
a[2] = 3
print(a,b)