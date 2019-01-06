from recursion import odd
List1 = [1,2,3,-4,6]

def maps(L):
    a = []
    for element in map(abs,List1):
        a.append(element)
    return a

print (maps(List1))

def maps2(L):
    b= []
    for i in map(odd, L):
        b.append(i)
    return b

print(maps2(List1))

def maps2lists(Lista, Listb):
    """ this function takes 2 lists and returns the minimum of the respective elements
    compared to each list"""
    results = []

    for elements in map(min, Lista,Listb):
        results.append(elements)

    return results

print (maps2lists([1,3,4,7],[2, 3, 5, 2]))


