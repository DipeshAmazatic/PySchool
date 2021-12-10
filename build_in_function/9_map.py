# map(function, iterable, ...) Apply function to every item of iterable and return a list.


# Complete the code below so that the outputs are as shown in the examples above.
def hex_value(num):
    return hex(num)
def mapfn1(alist):
   return list(map(hex_value,list(alist)))

def mapfn2(alist):
   return list(map(lambda x:x%2,list(alist)))

def mapfn3(word):
   return list(str(list(map(lambda x:x.upper(),word))[0]))


print(mapfn1(range(10, 13)))                       # convert to hex 
#['0xa', '0xb', '0xc']
print(mapfn2(range(10)))                           # modulo 2
#[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
print(mapfn3(['pyschools']))                       # convert to uppercase
#['P', 'Y', 'S', 'C', 'H', 'O', 'O', 'L', 'S']