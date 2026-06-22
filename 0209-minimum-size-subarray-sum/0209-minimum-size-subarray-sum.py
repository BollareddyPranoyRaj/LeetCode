class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        l=0
        mini=float('inf')
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                mini=min(mini,r-l+1)
                s-=nums[l]
                l+=1
        if mini < float('inf'):
            return mini
        return 0
        