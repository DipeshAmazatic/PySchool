# Write a function hasSameContent(t1, t2) that takes in two tuples as arguments and return True if 
# both tuples contain the same items.

def hasSameContent(t1, t2):
    if(len(t1)==len(t2)):
        t1=list(t1)
        for i in t2:
            if(i in t1):
                t1.remove(i)
            else:
                return False
        return True
    else:
        return False

print(hasSameContent((1, 2), (1, 2)))
print(hasSameContent((1, 2), (2, 1)))
print(hasSameContent((1, 2), (1, 2, 1)))
print(hasSameContent((1, 2), ()))