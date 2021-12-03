# list([iterable]) Return a list whose items are the same and in the same order as iterrable's items.

# Write down the values of variables b and c, with the output as shown in the above example.
b ="google"
c = "engine"
print(list(map(list, zip(list(b), list(c)))))