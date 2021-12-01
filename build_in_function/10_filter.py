# filter(function, iterable) Construct a list from items of iterable for which function returns True.

# Complete the code below so that the outputs are as shown in the examples above.
def lowercase(x):
    if(x>='a' and x<='z'):
        return x


def fn1(word):
   return ''.join(list(filter(lowercase, word)))

def fn2(word):
   return ''.join(list(filter(lambda x:x>='0' and x<='9',word) ))


print(fn1('aBCDefG'))
print(fn2('13a@b24&z'))