class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        x=set(candyType)
        y=len(x)
        return min(n,y)
