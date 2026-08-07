class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def canAssign(x):
            children = 0
            for pile in candies:
                children += pile // x
            return children >= k

        low, high = 1, max(candies)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if canAssign(mid):
                ans = mid
                low = mid + 1      # Try for a larger value
            else:
                high = mid - 1

        return ans
