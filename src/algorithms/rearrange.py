

from collections import Counter

def reorganizeString(s: str) -> str:
    '''
    Reorganize string so that no two adjacent chars are the same
    If not possible, return empty string
    
    greedy solution:
    - fill every other position with most frequent char
    - then fill in remaining positions with remaining chars (does not have to be greedy)
    - if at any point two adjacent chars are the same, return empty string
    - return the result
    '''

    counts = Counter(s)

    most_common_char, _ = counts.most_common(1)[0]
    
    res = [''] * len(s)
    i = 0

    while counts[most_common_char] > 0:
        if i >= len(s): 
            # ran out of space to put most common char
            return ""        
        res[i] = most_common_char
        i += 2
        counts[most_common_char] -= 1

    # fill in remaining positions with remaining chars
    for char, count in counts.items():
        while count > 0:
            if i >= len(s):
                i = 1
            res[i] = char
            if i > 0 and res[i] == res[i - 1]:
                return ""
            i += 2
            count -= 1

    return ''.join(res)

if __name__ == '__main__':
    s = "aaabbc"
    print(reorganizeString(s))  # e.g. "ababac" or "abcaba"
    