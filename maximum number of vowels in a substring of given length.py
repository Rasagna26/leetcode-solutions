class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v=set("aeiou")
        c=0
        for i in range(0,k):
            if s[i] in v:
                c+=1
        mv=c
        for i in range(k, len(s)):
            if s[i] in v:
                c += 1

            if s[i-k] in v:
                c -= 1
            mv=max(mv,c)
            
        return mv


        
            
        
