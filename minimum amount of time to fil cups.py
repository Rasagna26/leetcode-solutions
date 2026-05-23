class Solution:
    def fillCups(self, amount: List[int]) -> int:
        s=sum(amount)
        m=max(amount)
        return max(m,(s+1)//2)
