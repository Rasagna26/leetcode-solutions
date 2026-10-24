class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for ch in s:
            if len(ans) > 0 and ans[-1].lower() == ch.lower() and ans[-1] != ch:
                ans.pop()
            else:
                ans.append(ch)     
        return "".join(ans)
