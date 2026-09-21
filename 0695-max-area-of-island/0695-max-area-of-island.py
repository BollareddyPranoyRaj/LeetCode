from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        vis=set()
        q=deque()
        def bfs(i,j):
            dire=[[-1,0],[0,-1],[1,0],[0,1]]
            vis.add((i,j))
            q.append((i,j))
            area=1
            while q:
                x,y=q.popleft()
                for dr,dc in dire:
                    nr=x+dr
                    nc=y+dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr,nc) not in vis:
                        vis.add((nr,nc))
                        q.append((nr,nc))
                        area+=1
            return area 
        maxi=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1 and (i,j) not in vis:
                    area=bfs(i,j)
                    maxi=max(maxi,area)
        return maxi
                

        