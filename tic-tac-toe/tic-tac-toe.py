import datetime

class Player:
    def __init__(self, game_piece, name):
        self.game_piece = game_piece
        self.name = name

class Move:
    def __init__(self, author, position):
        self.author = author
        self.position = position

class Board:
    def __init__(self):
        self.moves = [["-","-","-"],["-","-","-"],["-","-","-"]]

    def display(self):
        for line in self.moves:
            print(f'{line[0]} {line[1]} {line[2]}')
    
    def add_move(self, move):
        row = move.position[0]
        column = move.position[1]
        self.moves[row][column] = move.author.game_piece

class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = None
        self.finished_at = None