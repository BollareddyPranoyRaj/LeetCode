class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        f=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    f+=1

        minu=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and f>0:
            s=len(q)
            for _ in range(s):
                i,j=q.popleft()
                for dr,dc in directions:
                    nr=i+dr
                    nc=j+dc
                    if nr<n and nc<m and  nr >= 0 and nc >= 0 and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append([nr,nc])
                        f-=1
            minu+=1
        if f>0:
            return -1
        return minu


        
        