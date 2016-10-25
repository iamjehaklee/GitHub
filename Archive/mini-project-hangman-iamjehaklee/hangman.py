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


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    """
    Check each letter in secretWord to see if the letters that are guessed match. If the letters match, then return True. If not, it is false. 
    """
    returnValue = ''
    for i1 in secretWord:
      letterFound = False
      for i2 in lettersGuessed:
        if i1 == i2:
          letterFound = True
      if letterFound == False:
        return False
    return True

# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    """
    For all values that were not guessed in lettersGuessed, add a '_ ' to signify that the letters were not found in the secretWord. For values that were guessed in
    secretWord, fill those letters in. 
    """
    returnValue = ''
    for i1 in secretWord:
      letterFound = False
      for i2 in lettersGuessed:
        if i1 == i2:
          letterFound = True
      if letterFound == False:
        returnValue = returnValue + '_ '
      else:
        returnValue = returnValue + i1
    return returnValue


# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.
    """
    Remove the lowercase letters that have been guessed so you prevent the person from guessing twice. 
    """
    # FILL IN YOUR CODE HERE...
    returnValue = string.ascii_lowercase
    for i in lettersGuessed:
      returnValue = returnValue.replace(i, '')
    return returnValue


# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


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
    print("--------------------------------------------------------")
    print("The word contains", len(secretWord), "letters.")

    """
    This part of the code creates the interactions portion of the game. Asks the user to input ONE letter. The lettersGuessed calls upon the getAvailableLetters function, which gives 
    the letters that have not been guessed yet. This keeps iterating until the game is completed.  
    """

    done = False
    lettersGuessed = []
    NumberofGuesses = 8
    print("You will start with 8 guesses.")
    while done == False and NumberofGuesses > 0:
      guess = input("Please supply a single letter for the next guess: ")
      if len(guess) != 1:
        print("Please only type one letter.")
        print("You have not guessed the following letters:", getAvailableLetters(lettersGuessed))
        print("--------------------------------------------------------")
      elif guess == ' ':
        print("Please type a valid letter.")
        print("You have not guessed the following letters:", getAvailableLetters(lettersGuessed))
        print("--------------------------------------------------------")
      else:
        if guess in lettersGuessed:
          print("Please choose a different letter!")
          print("You have", NumberofGuesses, "guesses left.")
        elif guess in secretWord:
          print("Your guess was in the word!")
          print("You have", NumberofGuesses, "guesses left.")
          lettersGuessed.append(guess)
        else:
          print("Your guess was not in the word!")
          NumberofGuesses = NumberofGuesses - 1 
          print("You have", NumberofGuesses, "guesses left.")
          lettersGuessed.append(guess)
        done = isWordGuessed(secretWord, lettersGuessed)
        if done == False:
          print(getGuessedWord(secretWord, lettersGuessed))
          print("You have not guessed the following letters:", getAvailableLetters(lettersGuessed))
          print("--------------------------------------------------------")
    if done:
      print("Congratulations, you won! The word is", secretWord,".")
    else:
      print("Sorry, you lost because you ran out of guesses :(. The word is", secretWord,".")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
