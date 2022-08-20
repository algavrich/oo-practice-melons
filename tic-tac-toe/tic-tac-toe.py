"""Tic tac toe game"""

# Import datetime to keep track of game times
from datetime import datetime

class Player:
    """Player class holds player name and game piece"""

    def __init__(self, game_piece, name):
        """Initialize game piece and name attributes"""

        self.game_piece = game_piece
        self.name = name

class Move:
    """Move class holds author object and position for given move"""

    def __init__(self, author, position):
        """Initialize author and position attributes"""

        self.author = author
        self.position = position

class Board:
    """Board class holds current board and can display baord and add move"""

    def __init__(self):
        """Initialize .moves object that hold moves on current board"""

        self.moves = [["-","-","-"],["-","-","-"],["-","-","-"]]

    def display(self):
        """Displays given board"""

        for line in self.moves:

            print(f'{line[0]} {line[1]} {line[2]}')
    
    def add_move(self, move):
        """Adds player's move to given board"""

        row = move.position[0]
        column = move.position[1]
        self.moves[row][column] = move.author.game_piece

class Game:
    """Game class holds given board, players, and time data"""

    def __init__(self, board, player1, player2):
        """Initialize board, player, and time log attributes"""

        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = None
        self.finished_at = None

    def check_for_winner(self):
        """Check if there is a winning board or draw
        
        If game over, announce winner/draw and return True
        """

        winner = None
        current_moves = self.board.moves

        # Check for winning row
        for row in current_moves:
            if row [0] != "-" and row[0] == row[1] and row[1] == row[2]:
                winner = row[0]
        
        # Check for winning column
        for i in range(3):
            if current_moves[0][i] != "-":
                if current_moves[0][i] == current_moves[1][i]:
                    if current_moves[1][i] == current_moves[2][i]:
                        winner = current_moves[0][i]

        # Check for winning first diagonal
        if current_moves[0][0] != "-":
            if current_moves[0][0] == current_moves[1][1]:
                if current_moves[1][1] == current_moves[2][2]:
                    winner = current_moves[0][0]

        # Check for winning second diagonal
        if current_moves[0][2] != "-":
            if current_moves[0][2] == current_moves[1][1]:
                if current_moves[1][1] == current_moves[2][0]:
                    winner = current_moves[0][2]

        # Check for draw
        if winner == None:
            if "-" not in current_moves[0]:
                if "-" not in current_moves[1]:
                    if "-" not in current_moves[2]:
                        winner = "Draw"
 
        # Do the thing if game is over (win or draw)
        if winner != None and winner != "Draw":
            if winner == "X":
                victor = self.player1
            else:
                victor = self.player2
            print(f"{victor.name} wins! Game over.")
            return True

        if winner == "Draw":
            print("Draw. Game over.")
            return True

        return False


def play_game():
    """Executes game play"""

    # Greet and get player names
    print("Initializing Game!")
    player_one_name = input("What's player one's name? ")
    player_two_name = input("What's player two's name? ")

    # Instantiate players and tell them their pieces
    player1 = Player("X", player_one_name)
    player2 = Player("O", player_two_name)
    print(f"{player1.name} is {player1.game_piece}")
    print(f"{player2.name} is {player2.game_piece}")

    # Instantiate board
    current_board = Board()
    
    #Instantiate game
    current_game = Game(current_board, player1, player2)

    # Log start time
    current_game.started_at = datetime.now()

    # Display guide board
    print("      Column 0  Column 1  Column 2")
    print("Row 0    -         -          -   ")
    print("Row 1    -         -          -   ")
    print("Row 2    -         -          -   ")

    while True:

        # Get player 1 move
        print("Player one, choose the location where you'd like to place your piece")
        print("What are the coordinates?")
        row = int(input("Row > "))
        column = int(input("Column > "))


        # Instantiate given move
        player_one_move = Move(player1, [row, column])

        # Add move to current board
        current_board.add_move(player_one_move)

        # Display current board
        current_board.display()

        # Check for winner and break if there is a winner
        if current_game.check_for_winner() == True:
            break

        # Get player 2 move
        print("Player two, choose the location where you'd like to place your piece")
        print("What are the coordinates?")
        row = int(input("Row > "))
        column = int(input("Column > "))

        # Instantiate given move
        player_two_move = Move(player2, [row, column])

        # Add move to current board
        current_board.add_move(player_two_move)

        # Display current board
        current_board.display()

        # Break if there is a winner
        if current_game.check_for_winner() == True:
            break


    current_game.finished_at = datetime.now()
    game_length = current_game.finished_at - current_game.started_at
    (print(f"Game Length: {game_length}"))

def actually_play_game():
    """PLay game until user wants to stop"""

    while True:

        play_game()

        print("Would you like to play again?")
        print("Type Y/n")
        while True:

            play_again = input("> ")

            if play_again.upper() == "Y":

                break

            elif play_again.lower() == "n":

                return "Game Over"

            else:

                print("That's not a valid answer")
                continue

actually_play_game()
            
