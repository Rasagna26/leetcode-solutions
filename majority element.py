from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=len(nums)
        freq=Counter(nums)
        for i in freq:
            if freq[i]>x//2:
                return i
