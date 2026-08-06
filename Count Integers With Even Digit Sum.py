class Solution:
    def countEven(self, num: int) -> int:
        def sum_of_digits(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        c = 0
        for i in range(1, num + 1):
            if sum_of_digits(i) % 2 == 0:
                c += 1

        return c
