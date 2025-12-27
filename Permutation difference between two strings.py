class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = {}
        
        # Store index of each character in t
        for i in range(len(t)):
            pos[t[i]] = i
        
        ans = 0
        # Compare positions
        for i in range(len(s)):
            ans += abs(i - pos[s[i]])
        
        return ans
