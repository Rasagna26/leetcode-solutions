class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        x=0
        for num in nums:
            if num%2==0:
                x|=num
        return x
