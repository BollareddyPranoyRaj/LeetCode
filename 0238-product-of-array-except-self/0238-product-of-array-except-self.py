class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sa=[0]*len(nums)
        pa=[0]*len(nums)
        pa[0]
        mul=1
        ans=[0]*len(nums)
        for i in range(len(nums)):
            mul*=nums[i]
            pa[i]=mul
        mul=1
        for i in range(len(nums)-1,0,-1):
            mul*=nums[i]
            sa[i]=mul
        for i in range(len(nums)):
            left=pa[i-1] if i>0 else 1
            right=sa[i+1] if i<len(nums)-1 else 1
            ans[i]=left*right
        return ans