# PART 1
# In the game of Yahtzee, players will roll 5 dice and score them. Scoring works like this:

# You can choose to score for 1s, 2s, 3s, 4s, 5s, or 6s.
# If you score for 1s, you get 1 point for every 1.
# If you score for 2s, you get 2 points for every 2. etc.

# For example, if you roll 4 2 2 5 5
# If you score for 5s, you get 10 points because there are two 5s and you get 5 for each 5.
# If you score for 2s, you get 4 points because there are two 2s and you get 2 for each 2.
# If you score for 4s, you get 4 points because there is only one 4 and you get 4 for each 4.
# If you score for 1s, you get 0 points because there are no 1s.

# Write a program that will generate 5 random numbers from 1 - 6.
# Then ask the player which number to score for and give them that score.
# Make your program have object-oriented design.


# PART 2
# In Yahtzee you can also score your dice in other ways:

# You get points if you have 3 of a kind or 4 of a kind.
# For example a roll of 3 4 2 2 2 gets you points for all these added together which is 13
# For example a roll of 5 5 5 5 1 gets you points for all these added together which is 21

# You get 50 points if you have 5 of a kind.
# For example a roll of 1 1 1 1 1 gets you 50 points for having five 1s.

# You get 25 points if you have a full house. A full house is 3 of a kind and 2 of a kind.
# For example a roll of 3 3 4 3 4 gets you 25 points because you have three 3s and two 4s.

# You get 30 points for having a small straight. This is when you have 4 numbers in a row.
# For example a roll of 1 4 3 2 4 is a small straight because you have numbers 1 - 4.

# You get 40 points for having a large straight. This is when you have 5 numbers in a row.
# For example a roll of 6 2 4 5 3 is a small straight because you have numbers 2 - 6.

# In addition to allowing the player to score for individual numbers, allow the player to score for 3/4/5 of a kind, full house, small/large straight.

from random import randint

class Die:
    def __init__(self):
        self.value = randint(1, 6)

    def roll(self):
        self.value = randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.dice = (Die() for _ in range(5))
        self.all_scores = []

    def roll_dice(self, keep=None):
        roll = []
        print("Rolling...")
        for die in self.dice:
            die.roll()
            roll.append(die.value)
        print(*roll)
        return roll

    def get_input(self):
        try:
            number = input('Enter a number to score: ')
            number = int(number)
            if number < 1 or number > 6:
                print("Please enter a number between 1 and 6.")
                return self.get_input()
            return number
        except TypeError:
            print("Please enter a number between 1 and 6.")
            return self.get_input()
        

    def get_score(self):
        roll = self.roll_dice()
        number = self.get_input()
        print(f'Keeping {number}')
        score = 0
        for n in roll:
            if n == number:
                score += n
        print(f'Score: {score}\n')
        return score

    def __str__(self):
        return self.name.upper()


class Yahtzee:
    def __init__(self, *players):
        if len(players) <= 1:
            print("Must have more than one player")
        self.players = (player for player in players)

    def turn(self):
        for player in self.players:
            print(player)
            player.get_score()
    


if __name__ == "__main__":
    player1 = Player('player1')
    player2 = Player('player2')
    game = Yahtzee(player1, player2)
    game.turn()
