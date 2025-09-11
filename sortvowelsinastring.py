class Solution:
    def sortVowels(self, s: str) -> str:
        arr=set('AEIOUaeiou')
        res=[]
        for ch in s:
            if ch in arr:
                res.append(ch)
        res.sort()
        idx=0
        ans=[]
        for ch in s:
            if ch in arr:
                ans.append(res[idx])
                idx+=1
            else:
                ans.append(ch)
        return ''.join(ans)

        
