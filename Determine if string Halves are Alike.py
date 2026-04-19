class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        
        mid = len(s) // 2
        first = s[:mid]
        second = s[mid:]
        
        count1 = sum(1 for ch in first if ch in vowels)
        count2 = sum(1 for ch in second if ch in vowels)
        
        return count1 == count2
