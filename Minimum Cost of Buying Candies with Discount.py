class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=1<<len(nums)
        ans=[]
        for i in range(subsets):
            lst=[]
            for j in range(len(nums)):
                if i&(1<<j):
                    lst.append(nums[j])
            ans.append(lst)
        return ans
