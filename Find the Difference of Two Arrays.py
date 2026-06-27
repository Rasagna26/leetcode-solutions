class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)

        x = list(a.difference(b))
        y = list(b.difference(a))

        res = []
        res.append(x)
        res.append(y)

        return res
