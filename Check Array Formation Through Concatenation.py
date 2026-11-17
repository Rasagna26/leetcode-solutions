class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        arr1 = []

        for num in arr:
            for i in range(len(pieces)):
                if pieces[i][0] == num:
                    arr1.extend(pieces[i])
                    break

        return arr1 == arr
