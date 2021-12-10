# min(iterable[, args...][, key]) Return the minimum item of a non-empty iterable or args. Optional key is a function
#  to convert each item before doing comparision.
# max works like min but returns the item with maximum value.

# Write a function that returns minimum and maximum values of a list containing numbers in integer and string formats.
def mixedList(mlist):
    max1=0
    min1=99999999999
    for i in mlist:
        if(int(i)>max1):
            max1=int(i)
        if(min1>int(i)):
            min1=int(i)
    return (min1,max1)


print(mixedList([0, '-2', '4', '13', 3]))