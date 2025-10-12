'''
simple multi-head target attention implementation in pytorch
'''

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from typing import Optional, Tuple

class TargetAttention(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0):
        '''
        Multi-head target attention layer.
        embed_dim: total dimension of the model
        num_heads: number of attention heads
        dropout: dropout probability on attention weights
        '''
        super(TargetAttention, self).__init__()
        assert embed_dim % num_heads == 0, "embed_dim must be divisible by num_heads"
        
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        self.dropout = nn.Dropout(dropout)
        
        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)
        
    def forward(self, query: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
        '''
        Forward pass for target attention.
        Inputs:
        query: (1, N, E) where L=1 (single target token), N is batch size, E is embedding dim
        key: (S, N, E) where S is source sequence length
        (no value input, value is identical to key in target attention)

        Returns:
        key items sum-pooled with attention weights w.r.t. query items
        '''
        # L = 1 (single target token)
        L, N, E = query.size()
        S = key.size(0)

        # Project inputs to multi-head QK
        q = self.q_proj(query).view(L, N * self.num_heads, self.head_dim).transpose(0, 1)  # (N*num_heads, 1, head_dim)
        k = self.k_proj(key).view(S, N * self.num_heads, self.head_dim).transpose(0, 1)    # (N*num_heads, S, head_dim)

        # Scaled dot-product attention
        attn_weights = torch.bmm(q, k.transpose(1, 2)) / math.sqrt(self.head_dim)  # (N*num_heads, 1, S)
        attn_weights = F.softmax(attn_weights, dim=-1)
        attn_weights = self.dropout(attn_weights)

        # Compute the weighted sum of values
        attn_output = torch.bmm(attn_weights, k)  # (N*num_heads, 1, head_dim)
        # Transpose to (1, N*num_heads, head_dim), then reshape to (1, N, E) to restore original dimensions
        attn_output = attn_output.transpose(0, 1).contiguous().view(L, N, E)  # (1, N, E)
        attn_output = self.out_proj(attn_output)  # (1, N, E)

        return attn_output
    
if __name__ == '__main__':
    # Example usage
    batch_size = 16
    embed_dim = 128
    num_heads = 4
    src_len = 1024

    model = TargetAttention(embed_dim, num_heads, dropout=0.1)
    query = torch.randn(1, batch_size, embed_dim)  # (1, N, E)
    key = torch.randn(src_len, batch_size, embed_dim)  # (S, N, E)

    output = model(query, key)
    print("Key shape:", key.shape)      # Should be (S, N, E)
    print("Query shape:", query.shape)  # Should be (1, N, E)
    print("Output shape:", output.shape)  # Should be (1, N, E)
    print("Output:", output)
