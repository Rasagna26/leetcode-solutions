class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        e = 0
        o = 1

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res[e] = nums[i]
                e += 2

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                res[o] = nums[i]
                o += 2

        return res
