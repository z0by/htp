# -*- coding: utf-8 -*-

"""
Sum square difference
Problem 6
---------------------------------------------------------
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sumDifference(*args):
    return abs(sum(x**2 for x in args) - sum(args)**2)

if __name__ == "__main__":
    #answer 25164150
    print sumDifference(*range(101))