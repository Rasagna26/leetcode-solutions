class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return false
        while n%3==0:
            n=n//3
        return n==1
