from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()   # combine words
        freq = Counter(words)             # count frequency
        
        res = []
        for word in freq:
            if freq[word] == 1:
                res.append(word)
        return res
