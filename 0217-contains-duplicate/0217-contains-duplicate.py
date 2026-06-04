class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hsh=set()
        n=len(nums)
        for i in nums:
            if i in hsh:
                return True
            else:
                hsh.add(i)
        return False


        