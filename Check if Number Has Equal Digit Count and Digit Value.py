from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i in range(len(num)):
            digit = str(i)
            if count[digit] != int(num[i]):
                return False
        return True
