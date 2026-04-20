from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(index, curr, current_sum):
            if current_sum == target:
                result.append(curr[:])
                return

            if index == len(candidates) or current_sum > target:
                return

            curr.append(candidates[index])
            helper(index, curr, current_sum + candidates[index])
            curr.pop()

            helper(index + 1, curr, current_sum)

        helper(0, [], 0)
        return result
