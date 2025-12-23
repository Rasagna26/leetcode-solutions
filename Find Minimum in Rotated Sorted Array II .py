class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                # min is in right half
                low = mid + 1
            elif nums[mid] < nums[high]:
                # min is in left half (including mid)
                high = mid
            else:
                # nums[mid] == nums[high], can't decide → shrink
                high -= 1

        return nums[low]
