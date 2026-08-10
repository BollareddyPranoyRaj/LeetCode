class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        nums = set(nums)

        i = 1
        while i <= len(nums) + 1:
            if i not in nums:
                return i
            i += 1