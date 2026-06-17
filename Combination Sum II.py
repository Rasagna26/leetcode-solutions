from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  

        def helper(index, curr, current_sum):
            if current_sum == target:
                result.append(curr[:])
                return

            if current_sum > target:
                return

            for i in range(index, len(candidates)):

               
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                helper(i + 1, curr, current_sum + candidates[i])  # move forward
                curr.pop()

        helper(0, [], 0)
        return result
