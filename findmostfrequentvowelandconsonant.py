class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter
        cnt=Counter(s)
        vow=set('aeiou')
        max_vowel=0
        max_consonant=0
        for i,c in cnt.items():
            if i in vow:
                if c>max_vowel:
                    max_vowel=c
            else:
                if c>max_consonant:
                    max_consonant=c
        return max_vowel+max_consonant
