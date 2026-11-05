class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num > 0:
                seen.add(num)
        if seen:
            return sum(seen)
        return max(nums)
