import cmath

def quadratic(a,b,c):
    x1 =  -(2*c)/b
    x2 = -b/a - x1
    return (x1,x2)

print quadratic(1,1,-6)