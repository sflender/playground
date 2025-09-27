'''
a simple class to simulate a tennis game scoring system.
'''

class TennisGame:
    def __init__(self):
        self.points = [0,15,30,40]
        self.score = [0, 0]  # [player1_score, player2_score]

    def won_point(self, player):
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
            return f"{self.points[self.score[0]]}-{self.points[self.score[1]]}" 


if __name__ == '__main__':
    game = TennisGame()
    while True:
        print("Current score:", game.get_score())
        player = int(input("Enter the player who won the point (1 or 2), or 0 to exit: "))
        if player == 0:
            break
        elif player in [1, 2]:
            game.won_point(player)
        else:
            print("Invalid input. Please enter 1, 2, or 0.")
    print("Final score:", game.get_score())