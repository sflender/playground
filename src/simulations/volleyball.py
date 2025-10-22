
from random import random

class Volleyball:
    def __init__(self, num_courts=3):
        self.max_points = 15  # 25 for regular games, 15 for short games
        self.courts = [ [0,0] for _ in range(num_courts) ]  # score per court
        self.is_ongoing = [True for _ in range(num_courts)] 
        self.num_finished = 0
        # court 0 has players 0-5, court 1 has players 6-11, etc.
        self.players = [ [ [i*6 + j for j in range(6)] , [i*6 + j for j in range(6,12)] ] for i in range(num_courts) ]
        self.previous_scoring_team = [None for _ in range(num_courts)]

    def step(self):
        # Simulate a rally on each court
        for i in range(len(self.courts)):
            if not self.is_ongoing[i]:
                continue  # Skip if the game is over
            scoring_team = 0 if random() < 0.5 else 1
            if self.previous_scoring_team[i] and self.previous_scoring_team[i] != scoring_team:
                # Rotate players on the scoring team
                self.players[i][scoring_team] = self.players[i][scoring_team][1:] + [self.players[i][scoring_team][0]]
            self.courts[i][scoring_team] += 1
            self.previous_scoring_team[i] = scoring_team
            # Check for game end condition (first to max_points with 2 point lead)
            if (self.courts[i][scoring_team] >= self.max_points and self.courts[i][scoring_team] - self.courts[i][1 - scoring_team] >= 2):
                self.is_ongoing[i] = False
                self.num_finished += 1

        print(self.courts)

if __name__ == "__main__":
    num_courts = 4
    vb = Volleyball(num_courts=num_courts)
    while True:
        vb.step()
        if vb.num_finished == num_courts:
            print("All games finished!")
            break