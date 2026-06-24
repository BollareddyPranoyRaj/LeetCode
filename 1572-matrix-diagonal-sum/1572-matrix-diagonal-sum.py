class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sum=0
        for i in range(n):
            j=i
            sum+=mat[i][j]
        j=len(mat[0])-1
        for i in range(n):
            sum+=mat[i][j]
            j-=1
        if len(mat)%2!=0:
            n=len(mat)//2
            m=len(mat[0])//2
            sum-=mat[n][m]
        return sum

        