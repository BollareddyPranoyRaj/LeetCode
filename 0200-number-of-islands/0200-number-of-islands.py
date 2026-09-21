from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        vis=set()
        q=deque()
        islands=0

        def bfs(i,j):
            dire=[[-1,0],[0,-1],[1,0],[0,1]]
            q.append((i,j))
            vis.add((i,j))
            while q:
                dr,dc=q.popleft()
                for x,y in dire:
                    nr=dr+x
                    nc=dc+y
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == "1" and (nr,nc) not in vis:
                        q.append((nr,nc))
                        vis.add((nr,nc))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i,j) not in vis:
                    bfs(i,j)
                    islands+=1
        return islands
