from random import randint

class Word :
    """A word that the game has chosen to be guessed by the player. 
    
    The responsibility of a Word is to control access to the list of potential words and to perform operation on that chosen word.
    Attributes:
        availableWords (list): The list of available words to guess from
        currentWord (string): The current word to guess
        maskedWord (string): The hidden word with only the correctly guessed letters shown
        
    Methods:
        getWord (string): sets a new word to guess and sets the coresponding masked word
        checkLetter(string): checks if the provided letter is in the currently chosen word
        getWordLength: returns the length of the currently chosen word
        completeMask: updates the maskedWord attribute with the completed letters filled in
        isWordComplete: returns true if the word is completly guessed
        printWord: prints the masked word to the screen with a space between each character
    """
    def __init__(self):
        self._availableWords = ['glasses', 'parachute', 'portuguese', 'family', 'catalogue', 'cat', 'simple', 'space']
        self._currentWord = ''
        self._maskedWord = '_'

    def getWord(self):
        self._currentWord = self._availableWords[randint(0, len(self._availableWords)-1)].lower()
        self._maskedWord = '_'*len(self._currentWord)

    def checkLetter(self, letter):
        if letter in self._currentWord:
            return True
        return False

    def getWordLength(self):
        return len(self._currentWord)

    def completeMask(self, letter):
        newMask = ''
        for i in range(len(self._currentWord)):
            if self._maskedWord[i] == '_' and self._currentWord[i] == letter:
                newMask += letter
            else:
                newMask += self._maskedWord[i]
        self._maskedWord = newMask

    def isWordComplete(self):
        if '_' in self._maskedWord:
            return False
        else:
            return True

    def printWord(self):
        printMe = ''
        for letter in self._maskedWord:
            printMe += letter
            printMe += ' '

        print(printMe)  
        print()
          