class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        ans=-1
        for num in nums:
            if num>0 and -num in nums:
                if num>ans:
                    ans=num
        return ans
