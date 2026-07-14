class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        arr=[0]*len(temp)
        st=[]
        for i in range(len(temp)):
            while st and temp[st[-1]]<temp[i]:
                arr[st[-1]]=i-st[-1]
                st.pop()
            st.append(i)
        return arr
        