class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        r = 0

        for x in range(left, right+1):
            y = x.bit_count()

            if y < 2:
                continue

            prime = True

            for i in range(2, int(y**0.5) + 1):
                if y % i == 0:
                    prime = False
                    break

            if prime:
                r += 1

        return r
