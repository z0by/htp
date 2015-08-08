def factorial(n):
    """
    Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    >>> factorial(30L)
    265252859812191058636308480000000L
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000L

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if n < 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    for x in xrange(1, int(n)+1):
        result = x*result
    return result


def factorial_recursive(n):
    """
    Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial_recursive(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial_recursive(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial_recursive(30)
    265252859812191058636308480000000L
    >>> factorial_recursive(30L)
    265252859812191058636308480000000L
    >>> factorial_recursive(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial_recursive(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial_recursive(30.0)
    265252859812191058636308480000000L

    It must also not be ridiculously large:
    >>> factorial_recursive(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """
    import math
    if n < 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    if n < 2:
        return 1
    else:
        return int(n)*factorial_recursive(int(n)-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
