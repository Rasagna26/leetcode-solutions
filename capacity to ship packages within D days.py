class Solution:
    def finddays(self, weights, capacity):
        days = 1
        load = 0

        for weight in weights:
            if load + weight > capacity:
                days += 1
                load = weight
            else:
                load += weight

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            noofdays = self.finddays(weights, mid)

            if noofdays <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low
