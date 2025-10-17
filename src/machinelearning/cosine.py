'''
Computes cosine similarity of two movies given their user ratings, where

cos(A, B) = (A · B) / (||A|| ||B||) 

where ||.|| denotes the L2 (Euclidian) norm.

Example input:
movie1 = {user1: 1, user2: 2}
movie2 = {user1: 1, user2: 1}

output: 0.8944 (approximate)

'''

from math import sqrt

def cosine_similarity(movie1: dict, movie2: dict) -> float:
    # Find common users
    common_users = set(movie1.keys()) & set(movie2.keys())
    
    if not common_users:
        return 0.0  # No common users, similarity is zero

    # Calculate dot product and magnitudes
    dot_product = sum(movie1[user] * movie2[user] for user in common_users)
    magnitude1 = sqrt(sum(rating ** 2 for rating in movie1.values()))
    magnitude2 = sqrt(sum(rating ** 2 for rating in movie2.values()))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  # Avoid division by zero

    return dot_product / (magnitude1 * magnitude2)

if __name__ == '__main__':
    # Example usage
    movie1_ratings = {'user1': 1, 'user2': 2, 'user3': 3}
    movie2_ratings = {'user1': 1, 'user2': 2, 'user3': 3}

    similarity = cosine_similarity(movie1_ratings, movie2_ratings)
    print(f'Cosine Similarity: {similarity:.4f}')