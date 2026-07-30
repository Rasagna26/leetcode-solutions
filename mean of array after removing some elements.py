class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        k = n // 20          
        arr = arr[k:n-k]     
        return sum(arr) / len(arr)
