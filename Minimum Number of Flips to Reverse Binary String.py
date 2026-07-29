class Solution:
    def minimumFlips(self, n: int) -> int:
        x = bin(n)[2:]
        y = x[::-1]

        c = 0

        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1

        return c 
