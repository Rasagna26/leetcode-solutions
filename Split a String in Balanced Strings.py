class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        r = 0
        
        for ch in s:
            if ch == 'L':
                c += 1
            else:
                c -= 1
            
            if c == 0:
                r += 1
        
        return r
