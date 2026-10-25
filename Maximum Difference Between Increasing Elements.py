class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        diff = -1
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                diff1 = nums[j] - nums[i]
                if diff1 > 0 and diff1 > diff:
                    diff = diff1
        return diff
