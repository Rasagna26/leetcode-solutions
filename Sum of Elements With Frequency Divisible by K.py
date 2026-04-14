from collections import Counter
from typing import List

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        total = 0
        
        for num in freq:
            if freq[num] % k == 0:
                total += num * freq[num]
                
        return total
