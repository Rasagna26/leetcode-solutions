class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x=len(bin(n))-2
        y=(1<<x)-1
        return int(n^y)
