class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=sorted(nums)
        d={}
        ans=[]
        for i in range(len(lst)):
            if lst[i] not in d:
                d[lst[i]]=i
        for num in nums:
            ans.append(d[num])
        return ans

