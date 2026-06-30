class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(nums)
        cols=len(nums[0])
        for i in range(rows):
            for j in range(i+1,cols):
                nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
        for row in nums:
            row.reverse()