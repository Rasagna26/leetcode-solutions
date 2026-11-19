class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = []
            d[nums[i]].append(i)

        count = 0

        for num in d:
            if len(d[num]) == 3:
                a, b, c = d[num]

                if b - a == c - b:
                    count += 1

        return count
