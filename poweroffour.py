class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return bool(0)
        while n%4==0:
            n=n//4
        return n==1
