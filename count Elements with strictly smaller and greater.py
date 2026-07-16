class Solution:
    def countElements(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)
        c=0
        for num in nums:
            if mn<num<mx:
                c+=1
        return c
