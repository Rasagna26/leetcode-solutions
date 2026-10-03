class Solution:
    def scoreOfString(self, s: str) -> int:
        r=0
        for i in range(len(s) - 1):
            r += abs(ord(s[i + 1]) - ord(s[i]))
        return r
