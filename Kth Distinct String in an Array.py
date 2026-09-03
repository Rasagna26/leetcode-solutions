class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        
        for s in arr:
            d[s] = d.get(s, 0) + 1

        lst = []

        for s in arr:
            if d[s] == 1:
                lst.append(s)

        return lst[k-1] if len(lst) >= k else ""
