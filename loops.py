
n = 0;
while n<7:
    print("While loop "+str(n))
    n=n+1


for i in range(5):
    print("For loop " + str(i))

mysum=0
for i in range(1,10,2):
    print("For loop sum "+ str(i))
    mysum = mysum+i
print(mysum)


mysum2 = 0
for i in range(5,20):
    mysum2= mysum2+i
    print(mysum2)
    if mysum2 == 27:
        break

print("My sum2 "+str(mysum2))



