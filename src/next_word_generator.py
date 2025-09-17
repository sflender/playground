
from collections import defaultdict, Counter

from numpy import random

class NextWordGenerator:
    def __init__(self):
        self.d = defaultdict(list)  # Maps a word to a list of possible next words

    def fit(self, text):
        words = [w.lower() for w in text.split()]
        for i in range(len(words) - 1):
            self.d[words[i]].append(words[i + 1])

        # d['hello'] = ['world','world','you']
        # d['hello'] = [['world','you'],[0.67,0.33]]

        for key in self.d.keys():
            counts = Counter(self.d[key])
            total = len(self.d[key])
            self.d[key] = [list(counts.keys()), [c / total for c in counts.values()]]

    def predict(self, word):
        if word not in self.d:
            return []
        
        words, probs = self.d[word]
        next_word = random.choice(words,p=probs)
        print(next_word)

model = NextWordGenerator()

text = 'hello world hello world hello you'

model.fit(text)

for _ in range(10):
    model.predict('hello')