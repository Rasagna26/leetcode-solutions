class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        wsize=n-k
        ws=sum(cardPoints[:wsize])
        mws=ws
        total=sum(cardPoints)
        for i in range(wsize,n):
            ws+=cardPoints[i]-cardPoints[i-wsize]
            mws=min(ws,mws)
        return total-mws
