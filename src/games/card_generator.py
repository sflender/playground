
import random
from itertools import combinations
from typing import List, Tuple


class Card:
    def __init__(self, features: List[str] = None):
        '''
        A card has three features: color, shape, number. Each feature can take one of three values.
        if features is provided, use it; otherwise, generate a random card.'''
        
        colors = ['red', 'blue', 'yellow']
        shapes = ['dots', 'stripes', 'squares']
        numbers = ['1', '2', '3']

        if features:
            self.features = features
        else:       
            self.features = [random.choice(feature) for feature in [colors, shapes, numbers]]


class Deck:
    def __init__(self):
        '''
        Generate a deck of all possible cards
        '''
        self.cards = [Card(features=[color, shape, number]) for color in ['red', 'blue', 'yellow']
                                           for shape in ['dots', 'stripes', 'squares']
                                           for number in ['1', '2', '3']]


def is_set(triple: Tuple[List[str], List[str], List[str]]) -> bool:
    """
    Return True if the given triple of cards forms a valid set.
    A set means that for each feature (color, shape, number), the
    three cards are either all the same or all different.
    """
    a, b, c = triple
    for i in range(len(a)):
        # all same or all different for this feature
        if not (a[i] == b[i] == c[i] or len({a[i], b[i], c[i]}) == 3):
            return False
    return True

if __name__ == '__main__':

    deck = Deck()
    print("number of cards in deck:", len(deck.cards))
    print("all possible cards:")
    for card in deck.cards:
        print(card.features)
        
    sets = []
    for triple in combinations(deck.cards, 3):
        features_triple = (triple[0].features, triple[1].features, triple[2].features)
        if is_set(features_triple):
            sets.append(features_triple)

    print(f"Total possilbe sets: {len(sets)}")
    print("All possbile sets:")
    for s in sets:
        print(s)
