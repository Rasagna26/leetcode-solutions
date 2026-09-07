class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}

        for i in str(n):
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        s = 0
        for i in freq:
            s += int(i) * freq[i]

        return s
