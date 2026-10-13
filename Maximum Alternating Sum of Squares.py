class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n=len(nums)
        mid=n//2
        osum=0
        for i in range(n):
            if i<mid:
                osum-=nums[i]**2
            else:
                osum+=nums[i]**2
        return osum
