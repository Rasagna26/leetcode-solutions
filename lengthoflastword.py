class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        x=a[-1]
        c=0
        for i in x:
            c+=1
        return c
