class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        l=0
        mini=float('inf')
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                mini=min(mini,r-l+1)
                sum-=nums[l]
                l+=1
        if mini < float('inf'):
            return mini
        return 0
        