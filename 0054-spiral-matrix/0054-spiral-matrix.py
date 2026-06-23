class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        t=0
        l=0
        b=len(m)-1
        r=len(m[0])-1
        ans=[]
        while l<=r and t<=b:
            for i in range(l,r+1):
                ans.append(m[t][i])
            t+=1
            for i in range(t,b+1):
                ans.append(m[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    ans.append(m[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    ans.append(m[i][l])
                l+=1
        return ans