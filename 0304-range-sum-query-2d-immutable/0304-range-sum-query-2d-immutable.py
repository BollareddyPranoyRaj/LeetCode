class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.mt=[[0]*len(self.matrix[0]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                left=self.mt[i][j-1] if j>0 else 0
                top=self.mt[i-1][j]  if i>0 else 0
                topLeft=self.mt[i-1][j-1] if i>0 and j>0 else 0
                self.mt[i][j]=self.matrix[i][j] + left + top - topLeft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.mt[row2][col2]
        top = self.mt[row1-1][col2] if row1 > 0 else 0
        left = self.mt[row2][col1-1] if col1 > 0 else 0
        topLeft = self.mt[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return total - top - left + topLeft

        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)