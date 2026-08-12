class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        s = set(nums)
        freq = Counter(nums)

        if k == 0:
            count = 0

            for x in freq:
                if freq[x] >= 2:
                    count += 1

            return count
        count = 0
        for x in s:
            if x + k in s:
                count += 1
        return count
