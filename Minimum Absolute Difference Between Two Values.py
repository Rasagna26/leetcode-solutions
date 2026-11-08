class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        diff=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]==1 and nums[j]==2:
                    diff.append(abs(i-j))
        if len(diff)>0:
            return min(diff)
        return -1
