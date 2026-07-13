class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s)-1):
            if abs(int(s[i+1])-int(s[i]))>2:
                return False
        else:
            return True
