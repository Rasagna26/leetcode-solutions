class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        c1=0
        c2=0
        for num in nums:
            if num>0:
                c1+=1
            elif num<0:
                c2+=1
        return max(c1,c2)
