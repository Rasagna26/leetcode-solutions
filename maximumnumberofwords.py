class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        broken=set(brokenLetters)
        c=0
        for i in text.split():
            if not(set(i) & broken):
                c+=1
        return c
