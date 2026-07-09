class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            if self.canmake(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low
    def canmake(self,bloomDay,day,m,k):
        bouquets=0
        flowers=0
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        return bouquets >= m
