from Pice import Pice

class Pawn(Pice):
    
    def __init__(self, id, side, figure, posX, posY, alive):
        super(Pawn, self).__init__(id, side, figure, posX, posY, alive)