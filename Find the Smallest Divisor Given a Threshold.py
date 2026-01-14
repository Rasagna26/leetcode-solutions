from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while (low<=high):
            mid=(low+high)//2
            sum=0
            for num in nums:
                sum+=ceil(num/mid)
            if(sum<=threshold):
                high=mid-1
            else:
                low=mid+1
        return low       
