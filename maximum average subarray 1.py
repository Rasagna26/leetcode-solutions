class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        l=0
        r=k-1
        wsum=sum(nums[0:k])
        maxsum=wsum
        while(r<n-1):
            wsum-=nums[l]
            l+=1
            r+=1
            wsum+=nums[r]
            if(wsum>maxsum):
                maxsum=wsum
        return maxsum/k
