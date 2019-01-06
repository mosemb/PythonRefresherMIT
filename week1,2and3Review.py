"""n = input("You are lost in the forest")
while n=='right':
    n=input("You are lost in the forest, go left or right?")
print("You got out the forest")
"""
""" 
n = 0
while n<5:
    print(n)
    n=n+1

for n in range(5):
    print(n)
"""
""" 
mysum = 0
for i in range(5,10):
    mysum = mysum+i
print(mysum )

"""
""" 
mysum = 0
for i in range(1,14,2):
    mysum = mysum+i
print(mysum)
"""

""" 
def g(y):
    x+1
    print(x+1)

x = 5
print(g(9))

"""


def g(x):
    def h():
        x="abc"
    x=x+1
    print(x)
    h()
    return x

print(g(3))
