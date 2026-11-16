class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s1=0
        s2=0
        for i in range(len(nums)):
            if i%2==0:
                s1+=nums[i]
            else:
                s2+=nums[i]
        return s1-s2
