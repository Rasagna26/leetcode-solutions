from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        min_diff = float('inf')

        # Step 1: find minimum difference
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff

        # Step 2: collect all pairs with that difference
        result = []
        for i in range(n - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result
