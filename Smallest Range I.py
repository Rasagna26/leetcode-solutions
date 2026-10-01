class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        maxi=max(nums)
        mini=min(nums)
        return max(0,maxi-mini-2*k)
