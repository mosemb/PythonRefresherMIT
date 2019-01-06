


def apply_to_all(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])

def mul_by_five(a):
    return a*5

test = [1, -4, 8, -9]

print(apply_to_all(test, mul_by_five))



def abs_va(a):
    """ Takes in alist and returns the absolute value of the the number """
    mut = []
    for i in range(len(a)):
        k= abs(a[i])
        mut.append(k)
    return mut

def add_li(a):
    """ takes a list and adds one to each element"""
    mut= [i * 5 for i in a]

    return mut



def square(a):
    """ Takes in a list and squares each element in the list"""
    mut = []
    for i in a:
        m = i**2
        mut.append(m)
    return mut

#print(square([1, -4, 8, -9]))

#print(apply_to_all(testList,abs_va))
