class Solution:
    def asteroidCollision(self, ass: List[int]) -> List[int]:
        st=[]
        for i in range(len(ass)):
            while st and ass[i]<0 and st[-1]>0 and abs(ass[i])>st[-1]:
                st.pop()
            if st and st[-1]>0 and ass[i]<0:
                if abs(ass[i])==st[-1]:
                    st.pop()
            else:
                st.append(ass[i])
        return st




        