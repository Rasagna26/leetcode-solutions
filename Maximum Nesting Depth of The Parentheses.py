class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        md=0
        for ch in s:
            if ch=="(":
                st.append(ch)
                md=max(md,len(st))
            if ch==")":
                st.pop()
        return md
