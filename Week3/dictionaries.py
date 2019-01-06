
dictrya = {'Ana':'C', 'James': 'D', 'Ricky': 'F'}

#Add and element

dictrya['Bob'] = 'A'

# Check presence of Bob in dictionary

bob= 'Bob'in dictrya
print(bob)

# Check presense of Dan in dictionary

dan = 'Dan' in dictrya

#print(dictrya['C'])

she_loves_you = she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

def lyrics_to_freq(lyrics):
    #Finds the number of words in lyrics. Takes in a list of lyrics.
    mydict = {}
    for word in lyrics:
        if word in mydict:
            mydict[word] +=1
        else:
            mydict[word]=1
    return mydict

def most_common_words(freq):
    values = freq.values()
    best = max(values)

    word = []
    for k in freq:
        print(k)
        if freq[k]==best:
            word.append(k)
    return (word, best)

def words_often_found(freq,mintimes):
    done = False
    results = []

    while not done:
        temp = most_common_words(freq)
        if temp[1] >=mintimes:
            results.append(temp)
            for w in freq:
                del(freq[w])
        else:
            done=True
    return results

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum = 0
    for i in aDict:
        k= len(aDict[i])
        sum = sum+k
    return sum

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    m = []
    for i in aDict:
        k = len(aDict[i])
        m.append(k)
        if k ==max(m):
            j=i
    return str(j)





animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati', 'hen','bull', 'eagle'], 'd':['geese', 'coachroach', 'cow']}

print(biggest(animals))















