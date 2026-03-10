class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        freq = {}
        
        # count numbers
        for row in grid:
            for num in row:
                freq[num] = freq.get(num,0) + 1
        
        repeat = -1
        missing = -1
        
        for i in range(1, n*n + 1):
            if i not in freq:
                missing = i
            elif freq[i] == 2:
                repeat = i
                
        return [repeat, missing]
