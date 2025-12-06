from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            # 1) Update the histogram heights for this row
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # 2) Compute largest rectangle area for current histogram
            max_area = max(max_area, self.maxRA(heights))
        
        return max_area

    def maxRA(self, heights: List[int]) -> int:
        n = len(heights)
        pse = self.PSE(heights)
        nse = self.NSE(heights)
        
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area

    def PSE(self, heights: List[int]) -> List[int]:
        # Previous Smaller Element (index)
        n = len(heights)
        stack = []
        ans = [0] * n
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(i)
        
        return ans

    def NSE(self, heights: List[int]) -> List[int]:
        # Next Smaller Element (index)
        n = len(heights)
        stack = []
        ans = [0] * n
        
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                ans[i] = n         # IMPORTANT: use n when no smaller on right
            else:
                ans[i] = stack[-1]
            stack.append(i)
        
        return ans
