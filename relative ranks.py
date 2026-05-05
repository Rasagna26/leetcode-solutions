from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = [(score[i], i) for i in range(n)]

        def heapify(arr, i, size):
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < size and arr[left][0] > arr[largest][0]:
                largest = left
            if right < size and arr[right][0] > arr[largest][0]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, largest, size)  

        def buildheap(arr):
            for i in range(n//2 - 1, -1, -1):
                heapify(arr, i, n)  

        buildheap(arr)

        res = [""] * n
        rank = 1
        size = n

        while size > 0:
            val, idx = arr[0]

            if rank == 1:
                res[idx] = "Gold Medal"
            elif rank == 2:
                res[idx] = "Silver Medal"
            elif rank == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank)

            arr[0], arr[size - 1] = arr[size - 1], arr[0]
            size -= 1

            heapify(arr, 0, size)

            rank += 1

        return res
