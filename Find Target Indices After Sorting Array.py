class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res=[]
        x=sorted(nums)
        for i in range(len(x)):
            if x[i]==target:
                res.append(i)
        return res
