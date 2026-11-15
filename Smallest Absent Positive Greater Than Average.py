class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        y = max(1, floor(avg) + 1)

        while y in nums:
            y += 1

        return y
