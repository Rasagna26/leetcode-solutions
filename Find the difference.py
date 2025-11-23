class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for ch in s + t:
            xor ^= ord(ch)
        return chr(xor)
