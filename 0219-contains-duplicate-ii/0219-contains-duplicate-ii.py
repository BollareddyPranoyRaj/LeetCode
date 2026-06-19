class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        if k == 0:
            return False
        for i in range(min(k,len(nums))):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        for i in range(len(nums)-k):
            if nums[i+k] in seen:
                return True
            seen.remove(nums[i])
            seen.add(nums[i+k])
        return False
                




            