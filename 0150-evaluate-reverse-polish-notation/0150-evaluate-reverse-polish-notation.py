class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i=='+':
                s=st.pop()+st.pop()
                st.append(s)
            elif i=='-':
                fir=int(st.pop())
                sec=int(st.pop())
                st.append(sec-fir)
            elif i=='/':
                fir=int(st.pop())
                sec=int(st.pop())
                st.append(int(sec/fir))
            elif i=='*':
                mul=st.pop()*st.pop()
                st.append(mul)
            else:
                st.append(int(i))
        return st.pop(0)
            
        