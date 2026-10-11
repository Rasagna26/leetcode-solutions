class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c = 0
        for i in range(len(fruits)):
            placed = False
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    placed = True
                    break
            if not placed:
                c += 1
        return c
