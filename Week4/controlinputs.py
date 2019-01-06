data = []
file_name = input("Enter file name")

try:
    fh = open(file_name,'r')
except IOError:
    print("File cant be found ")
else:
    for new in fh:
        if new !='\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()

    


