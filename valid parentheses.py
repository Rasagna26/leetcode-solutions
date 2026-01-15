class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in dict.values():
                stack.append(ch)
            else:
                if(len(stack)==0 or stack[-1]!=dict[ch]):
                    return False
                stack.pop()
        return len(stack)==0    
