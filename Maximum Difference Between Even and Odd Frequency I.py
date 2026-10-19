class Solution:
    def maxDifference(self, s: str) -> int:
        odd=[]
        even=[]
        for ch in s:
            count=s.count(ch)
            if count%2!=0:
                odd.append(count)
            else:
                even.append(count)
        return max(odd)-min(even)       
        
