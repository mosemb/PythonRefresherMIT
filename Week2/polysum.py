import math

def polysum(n,s):
    area = 0.25*n*s**2/(math.tan(math.pi/n))
    #sqr = area**2
    perimeter = n*s
    squareperimeter = perimeter**2
    sumarea = area+squareperimeter
    return float(str(round(sumarea, 4)))

print(polysum(11,70))