class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r=s[::-1]
        for i in range(len(s)-1):
            substring=s[i:i+2]
            if substring in r:
                return True
        return False
