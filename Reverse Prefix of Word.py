class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=word.find(ch)
        s=word[:i+1]
        return s[::-1]+word[i+1:]
