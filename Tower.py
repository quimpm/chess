from Pice import Pice

class Tower(Pice):
        
    def __init__(self, id, side, figure, alive):
        super(Tower, self).__init__(id, side, figure, alive)

    def display_moves(self,posX, posY, board):
        pass