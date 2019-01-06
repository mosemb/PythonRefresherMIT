
def quotient_remainder(x,y):
    q= x//y
    r = x%y
    return (q,r)

#(quotient,remainder)= quotient_remainder(5,

(quotient,remainder) = quotient_remainder(5,6)

def tuple_separate(aTuple):
    """ Tuple that separates words from numbers """
    num = ()
    words = ()

    for i in aTuple:
        num = num + (i[0],)
        if i[1] not in words:
            words = words + (i[1],)
    min_nums = min(num)
    max_nums = max(num)
    unique_words = len(words)

    return (min_nums,max_nums,unique_words)

tupleT = ((1,"one"),(2,"two"),(3 ,"three"),(4,"four"),(5,"five"))

#print(tuple_separate(tupleT))


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    tup = ()
    for i ,elements in enumerate(aTup):
        print (i)
        if i%2 == 0:
            tup = tup+(elements,)
    return tup

#print(oddTuples(("i", "love", "Rwanda", "its", "the", "best")))







