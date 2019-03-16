
'''
Write a Tic Tac Toe game played by only AI and only with random picks. 
Detect win or tie. 
Write a decorator to detect how fast a single game is played given a seed for random generation. 
Make sure to use only 1 random number per pick. 
Create another decorator to print out the Tic Tac Toe board at each 
pick so you can see what the AI is doing.
'''

import random
import time
# def printobject(obj):
#     """
#     obj -> object to be printed after function call
#     """
#     def decorator(func):
#         def wrapper(*args, **kwargs):    
#             return func(*args, **kwargs)
#         print(obj)
#         return wrapper

# def PrintGameBoard():
#     TicTacToe.__init__ = PrintBoard(TicTacToe, TicTacToe.play)

def logtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print("Completed '{0}' in {1}ms".format(func.__name__, time.time() - start_time))
    return wrapper


class printobject:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self, f):
        def wrapper(*args, **kwargs):    
            f(*args, **kwargs)
            print(self.obj)
        return wrapper


class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '] for _ in range(3)]
        self.players = [Player('X'), Player('O')]

    def place_letter(self, letter, row, col):
        self.board[row][col] = letter
        print()
        print(self)
        print()

    def turn(self, player):
        letter = player.letter
        row, col = player.pick_location()
        if self.board[row][col] is not ' ':
            return self.turn(player)
        self.place_letter(letter, row, col) 

    def is_win(self, player):
        for i in range(len(self.board)):
            if self.board[i][0] == player.letter and self.board[i][1] == player.letter and self.board[i][2] == player.letter:
                return True
            elif self.board[0][i] == player.letter and self.board[1][i] == player.letter and self.board[2][i] == player.letter:
                return True
            elif self.board[0][0] == player.letter and self.board[1][1] == player.letter and self.board[2][2] == player.letter:
                return True
            elif self.board[2][0] == player.letter and self.board[1][1] == player.letter and self.board[0][2] == player.letter:
                return True
        return False

    @logtime
    def play(self):
        for i in range(9):
            if i < 2:
                player = self.players[i]
            else:
                player = self.players[i%2]
            self.turn(player)

            if self.is_win(player):
                print(f'{player.letter} wins!')
                break

    def __str__(self):
        string = ''
        for i in range(len(self.board)):
            string += ' ' + ' | '.join(self.board[i])
            if i < 2:
                string += '\n-----------\n'
        return string


class Player:
    def __init__(self, letter):
        self.letter = letter
        random.seed(119)

    def pick_location(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return row, col


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
