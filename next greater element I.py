from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for x in nums1:
            index = nums2.index(x)   # find position in nums2
            found = -1

            for j in range(index + 1, len(nums2)):
                if nums2[j] > x:
                    found = nums2[j]
                    break

            ans.append(found)

        return ans
