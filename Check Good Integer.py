class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ss=0
        s=0
        while n>0:
            d=n%10
            ss+=d**2
            s+=d
            n=n//10
        return ss-s>=50
