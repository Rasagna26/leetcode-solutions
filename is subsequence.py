class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for ch in s:
            if ch in t:
                t = t[t.index(ch)+1:]
            else:
                return False
        return True
