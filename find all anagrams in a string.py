class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = {}
        for ch in p:
            freq[ch] = freq.get(ch, 0) + 1
        
        l = 0
        c = len(p)
        res = []
        
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    c -= 1
                freq[s[r]] -= 1
            
            if r - l + 1 > len(p):
                if s[l] in freq:
                    if freq[s[l]] >= 0:
                        c += 1
                    freq[s[l]] += 1
                l += 1
            
            if c == 0:
                res.append(l)
        
        return res
