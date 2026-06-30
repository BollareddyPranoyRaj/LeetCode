class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans
