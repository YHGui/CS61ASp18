""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def hailstone_helper(n, count):
    print(n)
    if n == 1:
        return count
    if n % 2 == 0:
        return hailstone_helper(n // 2, count + 1)
    else:
        return hailstone_helper(n * 3 + 1, count + 1)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    """
    # Without helper
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)
    """
    return hailstone_helper(n, 1)