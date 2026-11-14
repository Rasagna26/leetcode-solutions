class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        arr = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    discount = prices[j]
                    break
            arr.append(prices[i] - discount)
        return arr
