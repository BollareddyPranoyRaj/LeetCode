class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hsh={}
        for x in nums:
            if x not in hsh:
                hsh[x]=0
            hsh[x]+=1
        for x in hsh:
            if hsh[x]>len(nums)//2:
                return x 
        