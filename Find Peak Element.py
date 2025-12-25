class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low <high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[mid + 1]:
                # Peak is in left half including mid
                high = mid
            else:
                # Peak is in right half
                low = mid + 1
        
        return low
