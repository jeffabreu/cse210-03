class Player:
    """A person who plays the game. 
    
    The responsibility of a player is to guess letters, update the director when they are no longer playing.
    and check if they got a good guess or a bad guess.
    Attributes:
        isPlaying (boolean): Are you still playing the game?
        guessedLetter (string): The letter the player has guessed when last asked
        badGuesses (int): The number of guesses the player has made wrong
    Methods:
        getIsPlaying: returns the value of the isPlaying attribute
        setIsPlaying(boolean): sets the value of the isPlaying attribute
        guessLetter (string): Asks the player for a letter
        setBadGuesses (int): increments the number of guesses the player has made wrong
        getBadGuesses (int): Returns the number of wrong guesses the player has made
    """
    def __init__(self):
        self._isPlaying = True
        self._guessedLetter = ''
        self._badGuesses = 0

    def getIsPlaying(self):
        return self._isPlaying

    def setIsPlaying(self, isPlaying):
        self._isPlaying = isPlaying

    def guessLetter(self):
        self._guessedLetter = ''
        while not self._guessedLetter.isalpha():
            self._guessedLetter = input('Please Guess a Letter [a-z]').lower()
            print()
        return self._guessedLetter
        
    def setBadGuesses(self):
        self._badGuesses += 1

    def getBadGuesses(self):
        return self._badGuesses