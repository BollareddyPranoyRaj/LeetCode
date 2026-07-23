class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing=1
        nums.sort()
        for num in nums:
            if num > 0 and num == missing:
                missing+=1
        return missing