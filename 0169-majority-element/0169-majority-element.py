class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hsh={}
        n=len(nums)
        for i in nums:
            hsh[i]=hsh.get(i,0)+1
            if hsh[i] > (n//2):
                return i
        