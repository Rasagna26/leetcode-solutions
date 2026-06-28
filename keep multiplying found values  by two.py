class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num=set(nums)
        while original in num:
            original*=2
        return original
