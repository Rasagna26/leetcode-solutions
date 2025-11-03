class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = 0
        g = math.gcd(a, b)
        for i in range(1, int(g**0.5) + 1):
            if g % i == 0:
                c += 1
                if i != g // i:
                    c += 1
        return c
