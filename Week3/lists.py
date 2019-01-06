from recursion import recur_factorial , fib ,odd

def removedups(L1,L2):
    """ this is the wrong way to remove duplicates in a list because python removes every other item
    and forgets to update the previous element """

    for i in L1:
        if i in L2:
            L1.remove(i)
    return L1

a = [1, 2, 3, 4, 5 , 10, 11]
b = [1, 2, 3, 4, 8, 10, 11 ]
#print(removedups(a,b))

def copyremove(L1,L2):
    """ make a copy of L1 and they compare it with L2 then perform remove with L1"""
    L1_copy = L1[:]
    for i in L1_copy:
        if i in L2:
            L1.remove(i)
    return L1


clist = []

for i in a:
    if i in a:
        clist.append(i)


def apply_to_each(L, f):
    """ Takes a list and applies to each element the function """
    for i in range(len(L)):
        L[i]=f(L[i])
    return L

def apply_funcs(L,x):
    """ Takes a list of functions and applies a number to each one of them """
    for f in L:
        print(f(x))
    return L

L= [1,2,-5, -8 , 9.5]
#print('Apply abs function to list: ', apply_to_each(L,abs))
#print('Apply inf function to list: ', apply_to_each(L,int))
#print('Apply abs function to list: ', apply_to_each(L,abs))
#print('Apply factorial function to list: ', apply_to_each(L,recur_factorial))
#print('Apply odd function to list: ', apply_to_each(L,odd))
print( apply_funcs([abs, recur_factorial,fib, odd],4))



