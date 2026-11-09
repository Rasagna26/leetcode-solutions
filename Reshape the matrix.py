class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat
        arr = [x for row in mat for x in row]

        return [arr[i*c:(i+1)*c] for i in range(r)]
