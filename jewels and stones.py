class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=set(jewels)
        c=0
        for ch in stones:
            if ch in x:
                c+=1
        return c
