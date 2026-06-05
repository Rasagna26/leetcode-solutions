class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        n = abs(dividend)
        d = abs(divisor)

        quotient = 0

        while n >= d:
            cnt = 0

            while n >= (d << (cnt + 1)):
                cnt += 1

            quotient += (1 << cnt)
            n -= (d << cnt)

        return sign * quotient
