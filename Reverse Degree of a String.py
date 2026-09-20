class Solution:
    def reverseDegree(self, s: str) -> int:
        r=0
        for i in range(len(s)):
            index = ord('z') - ord(s[i]) + 1
            r+=(i+1)*index
        return r

