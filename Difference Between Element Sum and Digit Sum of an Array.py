class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=0
        e=0
        for num in nums:
            e+=num
            while num>0:
                d=num%10
                s+=d
                num=num//10
        return abs(e-s)
            
