class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s=0
        x=max(nums)
        for num in nums:
            s+=x-num
        return s
