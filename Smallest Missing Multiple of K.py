class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x=set(nums)
        for i in range(1,len(nums)+2):
            if k*i not in x:
                return k*i
        
