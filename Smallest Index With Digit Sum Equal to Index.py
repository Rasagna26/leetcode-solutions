class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=0
            x=nums[i]
            while x>0:
                d=x%10
                s+=d
                x//=10
            if i==s:
                return i
        return -1
