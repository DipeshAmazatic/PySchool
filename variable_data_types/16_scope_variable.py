"""Illustrating local and global variables."""
def changeval(x):
    """temp"""
    global Y_
    x = 3
    Y_ = 4

X = 1
Y_ = 2

changeval(X)

print(X)
print(Y_)
