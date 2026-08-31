class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v=set("aeiou")
        c=0
        for i in range(len(word)):
            s=set()
            for j in range(i,len(word)):
                if word[j] not in v:
                    break
                s.add(word[j])
                if len(s)==5:
                    c+=1
        return c
