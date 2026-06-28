class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(nums)
        col=len(nums[0])
        ans=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                ans[j][i]=nums[i][j]
        for i in range(row):
            ans[i].reverse()
        nums[:]=ans