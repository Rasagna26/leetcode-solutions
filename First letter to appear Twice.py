class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen=set()
        for ch in s:
            if ch not in seen:
                seen.add(ch)
            else:
                return ch
