try:
    a=int(input("Enter first element a "))
    b= int(input("Enter second element b "))
    c=a/b
    print(c)
    print("Okay")
except ValueError:
    print("Could not convert to number ")
except ZeroDivisionError:
    print("Could not divide by zero")
except:
    print("Something went really bad ")


while True:
    try:
        n=int(input("Please enter an int"))
        break
    except ValueError:
        print("Please enter an integer ")
print("Correct input of an integer ")








