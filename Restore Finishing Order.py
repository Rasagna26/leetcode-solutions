class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr=[]
        freq={}
        for num in friends:
            freq[num]=num
        for num in order:
            if num in freq:
                arr.append(num)
        return arr
