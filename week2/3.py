def eratosthenes(n):
    primes = []
    multiples = []
    for i in xrange(2, n+1):
        if i not in multiples:
            primes.append(i)
            multiples.extend(xrange(i*i, n+1, i))
    return (primes, multiples)
