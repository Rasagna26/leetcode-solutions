class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff=0
        for i in range(len(nums)):
            j=(i+1)%len(nums)
            diff=abs(nums[i]-nums[j])
            if diff>max_diff:
                max_diff=diff
        return max_diff
