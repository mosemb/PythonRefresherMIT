
s = ''.lower()
countvowel = 0
for i in s:
    if i == 'a' or i == 'e' or i=='o' or i == 'u' or i=='i':
        countvowel=countvowel+1

print('Number of vowels is: '+ str(countvowel))


