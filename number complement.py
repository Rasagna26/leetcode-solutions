class Solution:
    def findComplement(self, num: int) -> int:
        x=len(bin(num))-2
        y=(1 << x) - 1
        return int(num^y)
