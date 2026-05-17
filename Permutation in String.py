class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = {}
        for ch in s1:   # ✅ correct
            freq[ch] = freq.get(ch, 0) + 1
        
        l = 0
        count = len(s1)
        
        for r in range(len(s2)):   # ✅ correct
            
            # include right char
            if s2[r] in freq:
                if freq[s2[r]] > 0:
                    count -= 1
                freq[s2[r]] -= 1
            
            # shrink window if needed
            if r - l + 1 > len(s1):
                if s2[l] in freq:
                    if freq[s2[l]] >= 0:
                        count += 1
                    freq[s2[l]] += 1
                l += 1
            
            # check match
            if count == 0:
                return True
        
        return False
