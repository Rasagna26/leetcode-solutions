class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            if i % 2 == 0:
                arr2.append(nums[i])
            else:
                arr1.append(nums[i])

        arr1.sort(reverse=True)
        arr2.sort()

        res = []

        for i in range(len(arr1)):
            res.append(arr2[i])
            res.append(arr1[i])

        if len(arr2) > len(arr1):
            res.append(arr2[-1])

        return res
