class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        def helper(l,r,nums):
            if l>r:
                return -1
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            return helper(l,r,nums)
        return helper(l,r,nums)
        
        