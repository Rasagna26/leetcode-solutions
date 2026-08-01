class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        x=num
        while num>0:
            d=num%10
            if x%d==0:
                c+=1
            num=num//10
        return c
