class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        z=0
        ml=0
        for r in range(n):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[left]==0:
                    z-=1
                left+=1
            ml=max(ml,r-left+1)
        return ml
