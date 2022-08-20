######################
# Required Questions #
######################

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """

    if k > n:
        k = n
    a, b = 1, n - k
    while n > b: 
        a, n = a * n, n - 1
    return a 


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    for i in lst:
        if i != 0: 
            return i


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    return n in lst



def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    new = 1
    while n != 1:
        if n % 2 == 0: 
            n = n // 2
        elif n % 2 == 1: 
            n = (n * 3) + 1
        print(n)
        new += 1
    return new 

def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    if x % 2 == 0: 
        return 'even' 
    else: 
        return 'odd'

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """ 
    return [odd_even(i) for i in s]

def decode_helper(pair):
    """
    Optional helper function! Could be useful to turn something like [0, 0] to 'Male 0-9'
    """
    sex = ''
    if pair[0] == 0:
         sex = 'Male'
    elif pair[0] == 1:
        sex = 'Female'

    age = ''
    if pair[1] == 10:
        age = '100+'
    elif pair[1] < 10: 
        age = str(pair[1] * 10) + ('-') + str(pair[1] * 10 + 9)

    return sex + (' ') + age 
    

def decode(list_of_sex_age_pairs):
    """
    >>> decode([[0, 0], [1, 1], [1, 10]])
    ['Male 0-9', 'Female 10-19', 'Female 100+']
    >>> decode([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
    ['Male 0-9', 'Male 10-19', 'Male 20-29', 'Male 30-39', 'Male 40-49', 'Female 50-59', 'Female 60-69', 'Female 70-79', 'Female 80-89', 'Female 90-99', 'Female 100+']
    """ 
    return [decode_helper(i) for i in list_of_sex_age_pairs]

