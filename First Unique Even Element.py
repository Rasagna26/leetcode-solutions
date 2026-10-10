class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for num in nums:
            if num % 2 == 0 and nums.count(num) == 1:
                return num
        return -1
