
low = 0
high = 100
middle = (low+high)//2
for i in range(0,100):
    print('Please think of a number between 0 and 100!')
    print("Is your number "+ str(middle))
    guess = input(" If too high enter h , if too low enter l , i"
                      "if correct enter c ")
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



while True:
    print('Please enter a number between 0 and 100')
    guess = input("Please enter l for so low , h for so high and c for correct")

    if guess == 'l':
        low = middle
        middle = (high+low)//2
    elif guess == 'h':
        high = middle
        middle = (high+low)//2
    elif guess == 'c':
        print('Your number is '+str(middle))
        break
    else:
        print("We do not get it")

        




