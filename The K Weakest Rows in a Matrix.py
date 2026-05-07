class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=[(mat[i].count(1),i) for i in range(len(mat))]
        heap=[]
        res=[]
        for i in range(len(arr)):
            heapq.heappush(heap,arr[i])
        while k>len(res):
            x=heapq.heappop(heap)
            res.append(x[1])
        return res
