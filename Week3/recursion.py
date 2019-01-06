



def factorial(x):
    """ Factorial using a loop """
    prod = 1
    for i in range(1, x+1):
        prod *=i
        #print (prod)
    return prod

def recur_factorial(x):
    """ Factorial with recursion """
    if x==1:
        return x
    else:
        return x*factorial(x-1)

def odd(x):
    """ Returns True if x i odd"""
    return x%2!=0

def iterative_multiplication(a,b):
    """ Takes 2 numbers and gives back the product product is got iteratively"""
    result = 0
    while b>0:
        result = result+a
        b=b-1
    return result


def recursive_mutliplication(a,b):
    """ recursive multiplication , a is the recursive number b is the base """
    if b==1:
        return a
    else:
        return a+recursive_mutliplication(a,b-1)


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    prod = 1
    while exp>0:
        prod = prod*base
        exp=exp-1
    return prod


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if base==1:
        return exp
    else:
        return base*recurPower(base,exp-1)


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    y = max(a,b)
    values = []
    for i in range(1,y+1):
        if a%i ==0 and b%i==0:
            values.append(i)
    return (max(values))


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b==0:
        return a
    else:
        return gcdRecur(b, a%b)

def fib(x):
    """ if x =0 or 1 returns 1 or if not then returns the sum recursively """
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)


def isPalindorome(s):
    """ Takes a string and checks whether its a palindorome """
    def toChar(s):
        s=s.lower()
        ans= ''
        for character in s:
            if character in "abcdefghijklmnopqrstuvwxyz":
                ans=ans+character
        return ans

    def isPal(s):     #Recursive part of the algorithm
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1]and isPal(s[1:-1])

    return(isPal(toChar(s)))


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here


    if len(aStr)==0:
        return False
    elif len(aStr)==1:
        return aStr==char
    else:
        mid = len(aStr) // 2
        if char ==aStr[mid]:
            return True
        if char < aStr[mid]:
            return isIn(char, aStr[:mid])
        else:
            return isIn(char, aStr[mid+1:])




print(isIn('o','emby'))
#print (fib(2))
#print(gcdRecur(9,12))
#print(iterPower(5,3))
#print(iterPower(5,3))
#print(iterative_multiplication(6,6))





