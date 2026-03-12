class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        res = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = ""
        for ch, count in res:
            ans += ch * count

        return ans
