class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        dsum=0
        pro=1
        while temp>0:
            digit=temp%10
            dsum+=digit
            pro*=digit
            temp//=10

        return n%(dsum+pro)==0
                
