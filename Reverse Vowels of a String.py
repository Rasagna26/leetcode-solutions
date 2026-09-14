class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        vow = set('aeiouAEIOU')

        while l < r:
            if s[l] in vow and s[r] in vow:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vow and s[r] not in vow:
                r -= 1
            else:
                l += 1

        return ''.join(s)
