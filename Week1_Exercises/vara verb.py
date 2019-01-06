
"""
This script below returns statements based on either the value of Variable A and B.

"""


varA = 6
varB = 7

if type(varA)==str or type(varB) == str:
    print("There is a string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")

"""
The while loop below will print out the increments of a variable by 2 using the while loop till 
The condition is false. 
"""
num = 0
while num < 10:
    num = num + 2
    print(num)
print("Goodbye")


print ("Hello")
num = 10
while num>0:
    print(num)
    num = num-2


""" This sums up the values of the conditional till it terminates in descending order """
mysum3 = 0
nums = 0
while nums <3:
    nums = nums+1
    print(nums)
    mysum3 = mysum3 + nums

print("Mysum3 "+str(mysum3))
print(nums)


""" Incrementing for loop"""

for i in range(2,12,2):
    print(i)
print("Good bye ")

""" Decrementing for loop"""

print("Hello")
for i in range(10,0,-2):
    print(i)

end = 10
mysum6 = 0
for i in range(end+1):
    mysum6 = mysum6+i
print(mysum6)
















