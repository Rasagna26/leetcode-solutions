class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=1
        y=0
        for digit in str(n):
            d = int(digit)
            x*=d
            y+=d
        return x-y
