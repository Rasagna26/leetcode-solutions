class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                res.append(chr(num + 96))
                i -= 3
            else:
                num = int(s[i])
                res.append(chr(num + 96))
                i -= 1
                
        return "".join(res[::-1])
