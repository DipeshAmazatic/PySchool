"""For a quadratic equation in the form of ax2+bx+c, the discriminant,
D is b2-4ac. Write a function to compute the discriminant, D."""
def quadratic(a, b, c):
    return 'The discriminant is %s.'%(b**2-4*a*c)
print(quadratic(1, 2, 3))
print(quadratic(1, 3, 2))
print(quadratic(1, 4, 4))