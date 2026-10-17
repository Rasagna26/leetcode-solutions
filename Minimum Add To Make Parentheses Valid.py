class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        ans=0
        for ch in s:
            if ch=="(" :
                st.append(ch)
            else:
                if st:
                    st.pop()
                else:
                    ans+=1
        return len(st)+ans
