import numpy as np
import pandas as pd

def random_downsample_with_weights(df, n, weight_col):
    """
    Randomly downsample a DataFrame to n rows, using weights from weight_col.
    Uses binary search for efficient sampling.

    Args:
        df: pandas DataFrame to downsample
        n: number of rows to sample
        weight_col: column name in df containing weights

    Returns:
        Downsampled pandas DataFrame with n rows

    """

    weights = df[weight_col].to_numpy()
    weights = weights / np.sum(weights)  # normalize to sum to 1
    cum_weights = np.cumsum(weights)

    sampled_indices = set()
    while len(sampled_indices) < n:
        r = np.random.rand()
        # binary search to find the index where r would fit in cum_weights
        low, high = 0, len(cum_weights) - 1
        while low < high:
            mid = (low + high) // 2
            if cum_weights[mid] < r:
                low = mid + 1
            else:
                high = mid - 1
        sampled_indices.add(low)

    return df.iloc[list(sampled_indices)]

if __name__ == '__main__':

    # Example usage
    data = {
        'item': ['a', 'b', 'c', 'd', 'e'],
        'weight': [0.1, 0.5, 0.1, 0.1, 0.4]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)

    downsampled_df = random_downsample_with_weights(df, n=3, weight_col='weight')
    print("\nDownsampled DataFrame:")
    print(downsampled_df)