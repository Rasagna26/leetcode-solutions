class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c=0
        w=sum(arr[0:k])
        if w/k>=threshold:
            c+=1
        for i in range(k,len(arr)):
            
            w+=arr[i]
            w-=arr[i-k]
            avg=w/k
            if w and avg>=threshold:
                c+=1
        return c
