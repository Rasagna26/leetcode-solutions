class Solution:
    def greatestLetter(self, s: str) -> str:
        x = set(s)
        ans = ""

        for ch in x:
            if ch.lower() in x and ch.upper() in x:
                ans = max(ans, ch.upper())

        return ans
