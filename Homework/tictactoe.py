
'''
Write a Tic Tac Toe game played by only AI and only with random picks. 
Detect win or tie. 
Write a decorator to detect how fast a single game is played given a seed for random generation. 
Make sure to use only 1 random number per pick. 
Create another decorator to print out the Tic Tac Toe board at each 
pick so you can see what the AI is doing.
'''

import random

def PrintBoard(game, func):
    def wrapper(*args, **kwargs):
        print(game)
        return func(*args, **kwargs)
    return wrapper

def PrintGameBoard():
    TicTacToe.__init__ = PrintBoard(TicTacToe, TicTacToe.play)

def LogTime(func):
    def wrapper(*args, **kwargs):
        return
    return wrapper


class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None] for _ in range(3)]
        self.players = [Player('X'), Player('O')]

    def place_letter(self, letter, row, col):
        self.board[row][col] = letter

    def turn(self, player):
        letter = player.letter
        row, col = player.pick_location()
        if self.board[row][col] is not None:
            return self.turn(player)
        self.place_letter(letter, row, col) 

    def play(self):
        for i in range(9):
            if i < 2:
                player = self.players[i]
            else:
                player = self.players[i%2]
            self.turn(player)

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
        random.seed(1000)

    def pick_location(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return row, col


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
    # print(game)
