class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=0
        c2=0
        ans=[]
        for i in nums1:
            if i in nums2:
                c+=1
        ans.append(c)
        for i in nums2:
            if i in nums1:
                c2+=1
        ans.append(c2)
        return ans
