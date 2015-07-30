# -*- coding: utf-8 -*-

"""
Largest prime factor
Problem 3
------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(number):
    for x in xrange(2, int(number**0.5)+1):
        if number%x==0:
            return False
    else:
        return True

def get_largest(number):
    for x in xrange(2, int(number**0.5)+1):
        if number % x == 0 and  is_prime(x):
            yield x


if __name__ == "__main__":
    print(max(get_largest(600851475143)))
