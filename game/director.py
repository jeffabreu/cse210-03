from game.terminal_service import Word
from game.player import Player
from game.jumper import Jumper

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        player (Player): The Person playing the game
        isPlaying (boolean): Whether or not to keep playing.
        jumper (Jumper): The poor guy hanging from the parachute
        word (Word): controls the list of words and any actions taken on the word
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._player = Player()
        self._jumper = Jumper()
        self._word = Word()
        self._secretWord = self._word.getWord()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper.show_jumper(self._player.getBadGuesses())

        while self._player.getIsPlaying():
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """asks the player to make a guess.
        Args:
            self (Director): An instance of Director.
        """
        self._player.guessLetter()
        
    def _do_updates(self):
        """Keeps watch on how many wrong guesses the player has made and updates the masked word.
        and checks if the word has been completed successfully
        Args:
            self (Director): An instance of Director.
        """
        # If the player has guessed a letter correctly then update the mask
        if self._word.checkLetter(self._player._guessedLetter):
            self._word.completeMask(self._player._guessedLetter)
        else:
            self._player.setBadGuesses()
        
        # if the word has been completely guessed or the parachute man is dead
        if self._word.isWordComplete() or self._player.getBadGuesses() == 8:
            if self._player.getBadGuesses() == 8:
                self._jumper.showDeadMan()
            else:
                print('CONGRATULATIONS! You landed safely!')
            self._player.setIsPlaying(False)

    def _do_outputs(self):
        """prints the masked word to the terminal and the jumpers current state.
        Args:
            self (Director): An instance of Director.
        """
        
        self._word.printWord()
        self._jumper.show_jumper(self._player.getBadGuesses())
        