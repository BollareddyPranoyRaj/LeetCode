class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for x in reversed(nums):
            if x==val:
                nums.remove(val)
        return len(nums)
        
        