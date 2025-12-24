class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)          # total apples
        capacity.sort()                    # sort capacities
        current_capacity = 0
        boxes = 0

        # take largest boxes first
        for i in range(len(capacity)-1, -1, -1):
            current_capacity += capacity[i]
            boxes += 1
            if current_capacity >= total_apples:
                return boxes
