class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while st and k and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        while k:
            st.pop()
            k-=1
        res="".join(st).lstrip('0')
        return res if res else '0'

            
           

        