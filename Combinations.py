class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # base case
            if len(path) == k:
                result.append(path[:])
                return

            # try picking numbers from start to n
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result
