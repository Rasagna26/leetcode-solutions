class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(limit):
            count = 1
            curr = 0

            for num in nums:
                if curr + num <= limit:
                    curr += num
                else:
                    count += 1
                    curr = num

            return count <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left
