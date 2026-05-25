class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        ans = 0

        for count in freq.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1

        if ans < len(s):
            ans += 1

        return ans
