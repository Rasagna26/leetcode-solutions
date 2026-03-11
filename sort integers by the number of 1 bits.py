class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        
        for i in arr:
            ones = bin(i).count('1')
            res.append((ones, i))
            
        res.sort()
        
        return [i[1] for i in res]
