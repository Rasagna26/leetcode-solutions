class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        x=[i[::-1]for i in x]
        return " ".join(x)
