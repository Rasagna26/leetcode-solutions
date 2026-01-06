class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            res.append(nums[i] * nums[i])
        return sorted(res)
