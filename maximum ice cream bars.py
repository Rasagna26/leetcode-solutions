class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for num in costs:
            if coins>=num:
                coins-=num
                c+=1
            else:
                break

        return c
