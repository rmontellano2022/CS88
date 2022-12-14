## MapReduce
def map(f, s):
    """
    Map a function f onto a sequence.

    >>> def double(x):
    ...     return x * 2
    >>> def square(x):
    ...     return x ** 2
    >>> def toLetter(x):
    ...     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ...     return alpha[x%26]
    >>> map(double, [1,2,3,4])
    [2, 4, 6, 8]
    >>> map(square, [1, 2, 3, 4, 5, 10])
    [1, 4, 9, 16, 25, 100]
    >>> map(toLetter, [3, 0, 19, 0])
    ['d', 'a', 't', 'a']

    """
    if s == []:
        return s
    return [f(s[0])] + map(f, s[1:])


def filter(f, s):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    if len(s) == 1:
        return [s[-1]] if f(s[-1]) else []
    else:
        return filter(f, s[:-1]) + ([s[-1]] if f(s[-1]) else [])

from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    if base is None:
        base = s[0]
        s = s[1:]
    if len(s) == 0:
         return base
    return reduce(reducer, s[1:], reducer(base, s[0]))


# Recursive Math

def summation(n, term):
    """Return the sum of the 0th to nth terms in the sequence defined
    by term.
    Should be implemented using recursion.

    >>> summation(5, lambda x: x * x * x)
    225
    >>> summation(9, lambda x: x + 1)
    55
    >>> summation(5, lambda x: 2**x)
    63
    """
    if n <= 1:
        return n 
    else: 
        return summation(n) + summation(n-1, term)


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    >>> count_digit(1231421, 1)
    3
    >>> count_digit(12, 3)
    0
    """
    if n  < 10 and n == digit:
        return 1
    elif n < 10 and n != digit: 
        return 0 
    elif n % 10 == digit: 
        return 1 + count_digit(n // 10, digit)
    else: 
        return count_digit(n // 10, digit)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def func(n):
        if n < 10:
            return 0
        else: 
            return count_digit(10 - n % 10, n //10) + func(n // 10)
    return func(n)

