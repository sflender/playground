"""
a simple class to simulate a tennis game scoring system.
"""

class TennisGame:
    def __init__(self):
        self.points = [0,15,30,40]
        self.score = [0, 0]  # [player1_score, player2_score]

    def add_point(self, player):
        if player == 1:
            self.score[0] += 1
        elif player == 2:
            self.score[1] += 1

    def get_score(self):
        if self.score[0] >= 4 or self.score[1] >= 4:
            # advantage scoring
            if self.score[0] == self.score[1]:
                return "Deuce"
            elif self.score[0] == self.score[1] + 1:
                return "Advantage player 1"
            elif self.score[1] == self.score[0] + 1:
                return "Advantage player 2"
            elif self.score[0] >= self.score[1] + 2:
                return "Win for player 1"
            elif self.score[1] >= self.score[0] + 2:
                return "Win for player 2"
        else:
            p1 = self.points[self.score[0]] if self.score[0] < len(self.points) else self.points[-1]
            p2 = self.points[self.score[1]] if self.score[1] < len(self.points) else self.points[-1]
            return f"{p1}-{p2}"

class TennisSet:
    '''
    A set is won by the first player to win 3 games.
    '''
    def __init__(self):
        self.game = TennisGame()
        self.score = [0, 0]  # [player1_games_won, player2_games_won]

    def add_point(self, player):
        self.game.add_point(player)
        game_score = self.game.get_score()

        # check for game win
        if "Win for player 1" in game_score:
            self.game = TennisGame()  # reset game
            self.score[0] += 1
        elif "Win for player 2" in game_score:
            self.game = TennisGame()  # reset game
            self.score[1] += 1
        
        # check for set win
        if self.score[0] == 3:
            print("Player 1 wins the set!")
            self.score = [0, 0]  # reset set score
        elif self.score[1] == 3:
            print("Player 2 wins the set!")
            self.score = [0, 0]  # reset set score
        
        else:
            print("Current set score:", self.score)
            print("Current game score:", game_score)

if __name__ == '__main__':
    game = TennisSet()
    while True:
        player = int(input("Enter the player who won the point (1 or 2), or 0 to exit: "))
        if player == 0:
            break
        elif player in [1, 2]:
            game.add_point(player)
        else:
            print("Invalid input. Please enter 1, 2, or 0.")