class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        
        s = ""
        while num:
            s = str(num % 7) + s
            num //= 7
        
        if negative:
            s = "-" + s
        
        return s
