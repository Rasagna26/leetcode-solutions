from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for c in nums:
            stack.append(c)
            while len(stack)>=2 and gcd(stack[-1],stack[-2])>1:
                a=stack.pop()
                b=stack.pop()
                l=a*b//gcd(a,b)
                stack.append(l)
        return stack
