import math

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    d = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)

    return d

