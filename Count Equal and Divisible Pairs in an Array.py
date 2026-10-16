class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        c=0
        for l in range(len(nums)):
            for r in range(l+1,len(nums)):
                if nums[r]==nums[l] and (l*r)%k==0:
                    c+=1
        return c
