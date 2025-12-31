class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s=0
        for y in operations:
            if y=="++X" or y=="X++":
                s+=1
            else:
                s-=1
        return s
