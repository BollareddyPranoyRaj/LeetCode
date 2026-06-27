class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        ans=[[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                ans[j][i]=mat[i][j]
        return ans

