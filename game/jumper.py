class Jumper:
    """.
    
    The draw of the sticker in the screen, the jumper.
    Attributes:
        _man (list): a list containing each line of the parachute man
    """
    def __init__(self):
        #needs to be a list so it can be changed
        self._man = ['   ___   ','  /   \   ', '   ---   ','  \   /','   \ /   ','    0   ','   /|\   ','   / \    ']

    def show_jumper(self, lines):        
        # paints the jumper to the terminal screen
        x = lines-1
        while x < len(self._man)-1:
            x += 1 
            print(self._man[x])
        print()

    def showDeadMan(self):
        # paints the dead man to the screen
        self._man[5] = '    X   '
        self.show_jumper(5)
        print("OUCH! You didnt quite stick the landing!")