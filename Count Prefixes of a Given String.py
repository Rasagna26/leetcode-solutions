class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        c=0
        for i in range(len(s)):
            if s[:i+1] in words:
                c+=words.count(s[:i+1])
        return c
