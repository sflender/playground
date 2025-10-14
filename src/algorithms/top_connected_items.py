'''
design item-2-item topN counter. input is given as (user, item) pairs. function should take a
value n, and return the n items with the most connections to other items.

Example input:
(user, item)
1,A
1,B
1,C
2,A
2,D
3,A
3,B

output for n=2:
A (3 connections, A-B, A-C, A-D)
B (2 connections, B-A, B-C)
'''

from collections import defaultdict
import heapq
from typing import List, Tuple

def top_connected_items(pairs: List[Tuple[str, str]], n: int) -> List[Tuple[str, int]]:
    # Build a mapping from user to the set of items they interacted with
    user_to_items = defaultdict(set)
    for user, item in pairs:
        user_to_items[user].add(item)

    # Build a mapping from item to connected items
    item_connections = defaultdict(set)
    for items in user_to_items.values():
        # For each user, all their items are connected to each other
        items_list = list(items)
        for i, item1 in enumerate(items_list):
            for j, item2 in enumerate(items_list):
                if i != j:  # Don't connect item to itself
                    item_connections[item1].add(item2)

    # Use min-heap to maintain top n items
    min_heap = []
    
    for item, connections in list(item_connections.items())[:n]:
        connection_count = len(connections)
        heapq.heappush(min_heap, (connection_count, item))

    for item, connections in list(item_connections.items())[n:]:
        connection_count = len(connections)
        if connection_count > min_heap[0][0]:
            heapq.heappushpop(min_heap, (connection_count, item))

    return [(item, count) for count, item in sorted(min_heap, reverse=True)]

if __name__ == '__main__':
    # Example usage
    input_data = [
        ('1', 'A'),
        ('1', 'B'),
        ('1', 'C'),
        ('2', 'A'),
        ('2', 'D'),
        ('3', 'A'),
        ('3', 'B')
    ]
    n = 2
    result = top_connected_items(input_data, n)
    for item, count in result:
        print(f"{item} ({count} connections)")

