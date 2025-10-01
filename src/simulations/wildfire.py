
'''
a simple 2D simulation of a wildfire spreading over time
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from collections import deque

class Wildfire:
    # Neighbor offsets for 8-connected grid
    NEIGHBOR_OFFSETS = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),           (0, 1),
                        (1, -1),  (1, 0),  (1, 1)]  # 8-connected grid
    # NEIGHBOR_OFFSETS = [(-1,0),(1,0),(0,-1),(0,1)]  # 4-connected grid (no diagonals)

    def __init__(self, size: int = 50, p_tree: float = 0.6, p_fire: float = 0.01, 
                 p_regrow: float = 0.01, p_replicate: float = 0.02, p_spontaneous_fire: float = 0.001,
                 season_length: int = 50):
        '''
        Initialize the grid with trees and some initial fires.
        size: size of the grid (size x size)
        p_tree: probability of a cell being a tree
        p_fire: probability of a cell being on fire initially
        p_regrow: probability of empty cell regrowing into a tree
        p_replicate: probability of a tree spawning a new tree in neighboring cell
        p_spontaneous_fire: base probability of a tree spontaneously catching fire
        season_length: number of steps per season (4 seasons per cycle)
        '''
        self.size = size
        self.p_regrow = p_regrow
        self.p_replicate = p_replicate
        self.p_spontaneous_fire = p_spontaneous_fire
        self.season_length = season_length
        self.step_count = 0
        self.grid = np.zeros((size, size), dtype=int)  # 0: empty, 1: tree, 2: fire

        for i in range(size):
            for j in range(size):
                if random.random() < p_tree:
                    self.grid[i, j] = 1  # tree
                    if random.random() < p_fire:
                        self.grid[i, j] = 2  # fire

    def get_current_season(self):
        '''
        Return the current season based on step count.
        0: Spring, 1: Summer, 2: Fall, 3: Winter
        '''
        season_cycle = (self.step_count // self.season_length) % 4
        return season_cycle
    
    def get_season_name(self):
        '''Return the name of the current season.'''
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        return seasons[self.get_current_season()]
    
    def get_seasonal_fire_probability(self):
        '''
        Adjust spontaneous fire probability based on season.
        Summer: 2x higher, Winter: 0.5x lower, Spring/Fall: normal
        '''
        season = self.get_current_season()
        if season == 1:  # Summer
            return self.p_spontaneous_fire * 2.0
        elif season == 3:  # Winter
            return self.p_spontaneous_fire * 0.0  # No spontaneous fires in winter
        else:  # Spring (0) or Fall (2)
            return self.p_spontaneous_fire

    def step(self):
        '''
        Update the grid for one time step using a queue-based approach.
        Features:
        1. Fire spreads from burning trees to neighboring trees
        2. Burning trees become empty
        3. Empty cells can regrow into trees
        4. Trees can replicate to neighboring empty cells
        5. Trees can spontaneously catch fire
        '''
        # Increment step counter for seasonality
        self.step_count += 1
        
        # Get seasonal fire probability
        seasonal_fire_prob = self.get_seasonal_fire_probability()
        
        # Find all currently burning cells
        burning_cells = deque()
        new_fires = set()
        new_trees = set()
        
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i, j] == 2:  # burning tree
                    burning_cells.append((i, j))
        
        # Process fire spread and burning
        while burning_cells:
            i, j = burning_cells.popleft()
            
            # This burning tree becomes empty
            self.grid[i, j] = 0
            
            # Check neighbors for trees that should catch fire
            for di, dj in self.NEIGHBOR_OFFSETS:
                ni, nj = i + di, j + dj
                if (0 <= ni < self.size and 0 <= nj < self.size 
                    and self.grid[ni, nj] == 1):  # neighboring tree
                    new_fires.add((ni, nj))

        # Apply fire spread
        for i, j in new_fires:
            self.grid[i, j] = 2

        # Process regrowth, replication, and spontaneous fires
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i, j] == 0:  # empty cell
                    # Feature 1: Random regrowth
                    if random.random() < self.p_regrow:
                        new_trees.add((i, j))
                
                elif self.grid[i, j] == 1:  # tree
                    # Feature 3: Spontaneous fire (seasonal)
                    if random.random() < seasonal_fire_prob:
                        new_fires.add((i, j))
                    
                    # Feature 2: Tree replication
                    if random.random() < self.p_replicate:
                        # Try to spawn a tree in a random neighboring cell
                        neighbors = [(i + di, j + dj) for di, dj in self.NEIGHBOR_OFFSETS
                                   if 0 <= i + di < self.size and 0 <= j + dj < self.size]
                        if neighbors:
                            ni, nj = random.choice(neighbors)
                            if self.grid[ni, nj] == 0:  # empty neighbor
                                new_trees.add((ni, nj))

        # Apply new trees
        for i, j in new_trees:
            if self.grid[i, j] == 0:  # make sure it's still empty
                self.grid[i, j] = 1

        # Apply spontaneous fires (after tree creation to avoid immediate burning)
        for i, j in new_fires:
            if self.grid[i, j] == 1:  # make sure it's still a tree
                self.grid[i, j] = 2

    def run(self, steps: int = 100):
        '''
        Run the simulation for a given number of steps and visualize it.
        '''
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, cmap='coolwarm', vmin=0, vmax=2)
        fig.set_size_inches(fig.get_size_inches()[0]*2, fig.get_size_inches()[1]*2)
        
        # Add title to show current season
        title = ax.set_title('')

        def update(frame):
            self.step()
            img.set_array(self.grid)
            
            # Update title with current season and step count
            season = self.get_season_name()
            fire_prob = self.get_seasonal_fire_probability()
            title.set_text(f'Step {self.step_count} - {season} (Fire Risk: {fire_prob/self.p_spontaneous_fire:.1f}x)')
            
            return [img]
        
        ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, blit=False)
        plt.show()

if __name__ == '__main__':
    # Create a balanced ecosystem that can run indefinitely with seasons
    wildfire = Wildfire(
        size=100, 
        p_tree=0.6,           # initial tree density
        p_fire=0.01,          # initial fire probability
        p_regrow=0.005,       # regrowth rate (slow)
        p_replicate=0.02,     # tree replication rate
        p_spontaneous_fire=0.0005,  # base spontaneous fire rate
        season_length=50      # 50 steps per season (200 steps = 1 full year)
    )
    wildfire.run(steps=800)  # Run for 4 full years to see seasonal patterns