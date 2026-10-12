class Solution:
    def checkRecord(self, s: str) -> bool:
        c=0
        y=s.count("A")
        if y>=2:
            return False
        else:
            for ch in s:
                if ch=="L":
                    c+=1
                else:
                    c=0
                if c>=3:
                    return False
        return True
        
