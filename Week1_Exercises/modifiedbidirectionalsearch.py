x = 25
epsilon = 0.001
num_guesses = 0
low = 0.0
high = x
ans = (high+low)/2.0

while abs(ans**2-x)>=epsilon:
    print("low "+str(low)+ " high "+ str(high) + " ans "+ str(ans))
    num_guesses = num_guesses+1

    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2
print("Guesses "+ str(num_guesses))
print(str(ans) + " is close to the squareroot of "+ str(x))








