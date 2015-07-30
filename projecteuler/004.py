# -*- coding: utf-8 -*-

"""
Largest palindrome product
Problem 4
------------------------------
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrom(n):
    return str(n)==str(n)[::-1]

def get_largest_palindrom():
    return max([x*y for x in xrange(100,1000) for y in xrange(100,1000) if is_palindrom(x*y)])


if __name__ == "__main__":
    print((get_largest_palindrom()))
