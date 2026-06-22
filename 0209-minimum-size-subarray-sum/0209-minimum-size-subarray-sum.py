class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        l=0
        n=len(nums)
        mini=n+1
        for r in range(n):
            s+=nums[r]
            while s>=target:
                mini=min(mini,r-l+1)
                s-=nums[l]
                l+=1
        if mini != n+1:
            return mini
        return 0
        