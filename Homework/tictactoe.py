
'''
Write a Tic Tac Toe game played by only AI and only with random picks. 
Detect win or tie. Write a decorator to detect how fast a single game is played given a seed for random generation. 
Make sure to use only 1 random number per pick. Create another decorator to print out the Tic Tac Toe board at each 
pick so you can see what the AI is doing.
'''

import random

class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None] for _ in range(3)]

    def place_letter(self, letter, location):
        return


def LogTime(func):
    def wrapper(*args, **kwargs):
        return
    return wrapper

def PrintBoard():
    def wrapper():
        return
    return wrapper

game = TicTacToe()
print(game.board)
