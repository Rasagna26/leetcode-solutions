class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        
        while l<len(nums)-1:
            if nums[l]!=nums[l+1]:
                return nums[l]
            l+=2
        return nums[-1]   
