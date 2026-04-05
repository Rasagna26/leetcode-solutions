from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        ans = -1
        
        for num in freq:
            if num == freq[num]:
                ans = max(ans, num)
                
        return ans
