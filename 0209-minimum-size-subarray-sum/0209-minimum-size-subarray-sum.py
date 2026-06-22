class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        c=0
        mini=float('inf')
        l=0
        for r in range(len(nums)):
            sum+=nums[r]
            c+=1
            while sum>=target:
                mini=min(mini,c)
                sum-=nums[l]
                l+=1
                c-=1
        if mini < float('inf'):
            return mini
        return 0
        