'''
Implementation of SIM (search-based interest modeling) Hard Search 
Shrinks user action sequence from L to l by filtering for items with topics that match the target item
'''

import torch
import torch.nn as nn
import torch.nn.functional as F

class SIMHardSearch(nn.Module):
    def __init__(self):
        '''
        SIM layer to shrink user action sequence based on target item.
        no learnable parameters (it is completely non-parametric)
        '''
        super(SIMHardSearch, self).__init__()

    def forward(self, user_seq: torch.Tensor, target_item: torch.Tensor,
                user_seq_topics: torch.Tensor, target_item_topic: torch.Tensor, top_k:int) -> torch.Tensor:
        
        '''
        Forward pass for SIM layer.
        Inputs:
        user_seq: (L, B) where L is user sequence length, B is batch size
        target_item: (B) where 1 is single target item
        user_seq_topics: (L, B) topic indices for each item in user sequence
        target_item_topic: (B) topic index for target item
        top_k: number of items to select from user sequence

        Returns:
        shrunk_user_seq: (l, B) where l=top_k is the shrunk user sequence length
        '''
        L, B = user_seq.size()

        # create binary mask indicating topic matches
        mask = (user_seq_topics == target_item_topic.unsqueeze(0))  # (L, B)
        filtered_seq = []
        for b in range(B):
            matched_items = user_seq[mask[:, b], b]  # items in user_seq with matching topic
            if len(matched_items) >= top_k:
                filtered_seq.append(matched_items[:top_k])
            else:
                # pad with zeros if not enough matches
                padding = torch.zeros(top_k - len(matched_items), dtype=user_seq.dtype)
                filtered_seq.append(torch.cat([matched_items, padding], dim=0))
        shrunk_user_seq = torch.stack(filtered_seq, dim=1)  # (top_k, B)
        return shrunk_user_seq  # (top_k, B)
    
# Example usage:
if __name__ == '__main__':
    L, B, = 5, 2 # user sequence length, batch size
    user_seq = torch.tensor([
        [10, 20],
        [11, 21],
        [12, 22],
        [13, 23],
        [14, 24],
    ], dtype=torch.long)  # (L, B)
    user_seq_topics = torch.tensor([
        [1, 2],
        [1, 3],
        [2, 2],
        [2, 3],
        [3, 2],
    ], dtype=torch.long)  # (L, B)
    target_item = torch.tensor([12, 22], dtype=torch.long)  # (B,)
    target_item_topic = torch.tensor([1, 2], dtype=torch.long)  # (B,)
    top_k = 3

    sim_layer = SIMHardSearch()
    shrunk_seq = sim_layer(user_seq, target_item, user_seq_topics, target_item_topic, top_k)
    print("Input user sequence and topics:")
    print(user_seq)    # (L, B)
    print(user_seq_topics)  # (L, B)
    print("Target items and topics:")
    print(target_item)  # (B,)
    print(target_item_topic)  # (B,)
    print(f"Shrunk user sequence to top {top_k} items with matching topics:")
    print(shrunk_seq)  # (top_k, B)