
def divs(L1,L2):
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/float(L2[i]))
        except ZeroDivisionError:
            ratios.append(float("NaN"))
        except:
            raise ValueError('Get ratios called with bad arguments')
    return ratios

print(divs([1,3,4,4],[1,3,5,0]))

