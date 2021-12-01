# zip([iterable, ...]) Return a list of tuples, where the i-th tuple contains the i-th element from each of the iterables.

#Which of the codes below gives the following output?
a = [1, 2, 3]
b = 'abc'
#c
#[((1, 'a'), ('a', 1)), ((2, 'b'), ('b', 2)), ((3, 'c'), ('c', 3))]
c = zip(zip(a, b), zip(b, a))
print(list(c))