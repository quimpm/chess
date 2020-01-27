from Board import *
from Chess import *
from Player import *

class Game:

    def __init__ (self,chess,board):
        self.chess = chess
        self.board = board
        self.player1 = Player('1','white')
        self.player2 = Player('2','black')
        self.turn = self.player1

    def start_game(self):
        self.chess.board.bind("<Button-1>", self.click_handler)

    def click_handler(self,event):
        posX = self.chess.size_to_x_coordinates(event.x)
        posY = self.chess.size_to_y_coordinates(event.y)
        if self.board.containsPlayerPice(posX, posY, self.turn):
            self.board.actualizeMoves(posX, posY)
        elif self.board.isMoveCell(posX,posY):
            self.board.movePice(posX,posY)
        else:
            print('Yoyo, chill let me alone')
        self.chess.displayPices(self.board)
    def changeTurn():
        if self.turn.equals(self.player1):
            self.turn = self.player2
        else:
            self.turn = self.player1