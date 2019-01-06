
print("Please think of a number between 0 and 100!")

number = 8
epsilon = 0.001
num_guesses = 0
low = 0
high = 100
ans= (high+low)/2

while ans-number>=epsilon:
    print("low " + str(low) + " high " + str(high) + " ans " + str(ans))
    num_guesses=num_guesses+1
    if ans <=number:
        low=ans
    else:
        high=ans
    ans = (high+low)/2

print('Guesses '+ str(num_guesses))
print(ans)





