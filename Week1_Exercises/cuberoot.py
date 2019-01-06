cube = 29
epsilon = 0.0001
guess = 3
increment = 0.001
num_guesses = 0


while abs(guess**3-cube)>=epsilon and guess <=cube:
    guess = guess+increment
    num_guesses= num_guesses+1
    print("Guesses are "+str(num_guesses))
if abs(guess**3-cube)>epsilon:
    print("Failed on cube root of",cube)
else:
    print(guess, "is close to cube root of ",cube)




