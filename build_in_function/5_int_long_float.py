# int([x[,radix]]) Convert a string or number to a plain integer. radix has a default value of 10, can be [2, 36] or 0. 
# It can be given only if x is a string.
# long([x[,radix]]) Convert a string or number to a long integer. Otherwise, it is largely similar to int function.
# float([x]) Convert a string or a number to floating point.

#What are the values of a, b, c and d?
a = int('12', 8)
b = int('10100', 2)
c = float(a/b)
d = float(a)/b
print(a,b,c,d)