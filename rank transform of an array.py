class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}
        sorted_arr = sorted(set(arr))

        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1

        res = []

        for num in arr:
            res.append(rank[num])

        return res
