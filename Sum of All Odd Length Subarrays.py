class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        t=0
        n=len(arr)
        for i in range(n):
            for j in range(i,n):
                length=j-i+1
                if length%2==1:
                    t+=sum(arr[i:j+1])
        return t
