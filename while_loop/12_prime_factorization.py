"""Given a positive integer, write a function that computes the prime factors that can
be multplied together to get back the same integer."""
import operator
import functools as fun
def primeFactorization(num):
    primes = []
    result = []
    if num > 1:
        [primes.append(x) for x in range(2, num) if all(x % y != 0 for y in range(2, x))]
    multy = fun.reduce(operator.mul, result, 1)
    for number in primes:
        if num % number == 0 and multy != num:
            result.append(number)
    return result

print(primeFactorization(60))
print(primeFactorization(1050))
print(primeFactorization(1))