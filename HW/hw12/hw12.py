def naturals(initial = 1, step = 1):
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = initial
    while True:
        yield i
        i += step

class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

    def __iter__(self):
        self.current = self.start
        return self

def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1 and
    make sure to remove the repeated values in both.
    You can also assume that s0 and s1 represent infinite sequences.

    >>> twos = naturals(initial = 2, step = 2)
    >>> threes = naturals(initial = 3, step = 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    "*** YOUR CODE HERE ***"
    while True:
        if e0 == e1:
            yield e0
            e0 = next(i0)
            e1 = next(i1)
        elif e0 < e1:
            yield e0
            e0 = next(i0)
        else:
            yield e1
            e1 = next(i1)

