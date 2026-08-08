class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def pro(n):
            p=1
            while n>0:
                d=n%10
                p*=d
                n=n//10
            return p
        while pro(n) % t != 0:
            n += 1

        return n
