low = 0
high = 100
middle = (low+high)//2

print('Please enter a number between 0 and 100!')

while True:

    print("Is your secret number "+ str(middle))
    guess = input("Please enter l for so low , h for so high and c for correct ")


    if guess=='h' :
        high = middle
        middle = (high+low)//2

    elif guess =='l':
        low = middle
        middle = (high+low)//2

    elif guess == 'c':
        print('Your number is '+str(middle))
        break

    else:
        print('We do not get it')
        middle = (high+low)//2