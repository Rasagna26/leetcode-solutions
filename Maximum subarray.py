class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxx=float("-inf")
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maxx:
                maxx=sum
            if sum<0:
                sum=0
        return maxx
        
