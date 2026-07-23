class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        find = [False] * (n + 1)
        for x in nums:
            if 0 < x <= n:
                find[x] = True
        
        for i in range(1, n + 1):
            if not find[i]:
                return i
        
        return n + 1