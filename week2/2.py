import math
import cmath


def square_root(a, b, c):
    discr = b**2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return (x1, x2)
    elif discr == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + cmath.sqrt(discr)) / (2 * a)
        x2 = (-b - cmath.sqrt(discr)) / (2 * a)
        return(x1, x2)
