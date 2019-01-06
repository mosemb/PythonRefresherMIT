# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

#print(chooseWord(wordlist))

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    sorte = list(secretWord)
    guess = []
    for i in lettersGuessed:
        if i in secretWord:
            guess.append(i)
    return sorted(guess) == sorted(sorte)
#print(isWordGuessed('mole', ['m','k', 'o', 'l', 'e']))
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    lista = []
    for i, letters  in enumerate(secretWord):
        if letters in lettersGuessed:
            b = letters
            lista.append(b)
        else:
            b = "_ "
            lista.append(b)
    return "".join(lista)

#print(getGuessedWord('mikes',['m','e','o','f','g','k']))



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    d = []
    a = string.ascii_lowercase
    m = list(a)
    for i in m:
        if i not in lettersGuessed:
            d.append(i)
    return "".join(d)

#print(getAvailableLetters(['a','d','f']))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord))+ " letters long.")
    print("-------------")
    guess =8
    lettersGuessed =[]


    while guess<9 and guess>=0:
        if getGuessedWord(secretWord,lettersGuessed) == secretWord:
            print("Congratulations, you won! ")
            break
        elif getGuessedWord(secretWord,lettersGuessed)!=secretWord and guess==0:
            print("Sorry, you ran out of guesses. The word was "+str(secretWord)+".")
            break

        print("You have "+ str(guess)+ " Guesses left")
        letters = getAvailableLetters(lettersGuessed)
        wordguessed = isWordGuessed(secretWord, lettersGuessed)
        print("Available letters are: ",letters)

        userinput=input("Please guess a letter ")
        lettersGuessed.append(userinput)

        if userinput in secretWord and userinput in letters and wordguessed==False:
            print('Good guess: ', getGuessedWord(secretWord,lettersGuessed))
            guess = guess
            print("-------------")

        elif userinput not in letters:
            print("Oops! You've already guessed that letter: ",getGuessedWord(secretWord,lettersGuessed))
            guess=guess
            print("-------------")

        elif userinput not in secretWord and userinput in letters:
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord,lettersGuessed))
            print("-------------")
            guess= guess-1












        #else:
            #guess -=guess

















print(hangman(chooseWord(wordlist)))







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
