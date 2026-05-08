from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def heapify(arr, i, n):
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, largest, n)

        def heapify_up(arr, i):
            parent = (i - 1) // 2
            if i > 0 and arr[parent] < arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                heapify_up(arr, parent)

        n = len(stones)

        for i in range(n//2 - 1, -1, -1):
            heapify(stones, i, n)

        while len(stones) > 1:
            stones[0], stones[-1] = stones[-1], stones[0]
            y = stones.pop()
            heapify(stones, 0, len(stones))

            stones[0], stones[-1] = stones[-1], stones[0]
            x = stones.pop()
            heapify(stones, 0, len(stones))

            if y != x:
                stones.append(y - x)
                heapify_up(stones, len(stones)-1)

        return stones[0] if stones else 0
