from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = nums.index(max(nums))   # index of largest number
        
        for i in range(len(nums)):
            if i != x and nums[x] < 2 * nums[i]:
                return -1
        
        return x
