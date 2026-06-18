from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def helper(start, curr, total):
           
            if total == n and len(curr) == k:
                result.append(curr[:])
                return
            
            if total > n or len(curr) > k:
                return

            for i in range(start, 10): 
                curr.append(i)
                helper(i + 1, curr, total + i)
                curr.pop()

        helper(1, [], 0)  
        return result
