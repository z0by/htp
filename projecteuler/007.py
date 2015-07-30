# -*- coding: utf-8 -*-

"""
10001st prime
Problem 7
----------------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def brutforce():
    num = 2
    count = 0
    while True:
        for x in xrange(2, int(num**0.5)+1):
            if num % x == 0:
                num +=1
                break
        else:
            count +=1
            if count == 10001:
                print num
                break
            num +=1

#решето Эратосфена
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q

            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1



if __name__ == "__main__":
    count = 0
    for x in gen_primes():
        count +=1
        if count == 10001:
            print x
            break

