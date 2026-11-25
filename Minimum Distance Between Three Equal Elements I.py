class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_dis = float('inf')
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dis = abs(i-j) + abs(j-k) + abs(k-i)
                        min_dis = min(min_dis, dis)

        return min_dis if min_dis != float('inf') else -1
