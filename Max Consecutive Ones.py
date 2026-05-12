class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        ml=0
        for n in nums:
            if n==1:
                c+=1
                ml=max(c,ml)
            else:
                c=0
        return ml
