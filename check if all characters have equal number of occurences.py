class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict={}
        for ch in s:
            dict[ch]=dict.get(ch,0)+1
        return len(set(dict.values()))==1
