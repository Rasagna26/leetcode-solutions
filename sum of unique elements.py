from collections import Counter
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        total = 0
        
        for num in freq:
            if freq[num] == 1:
                total += num
                
        return total
