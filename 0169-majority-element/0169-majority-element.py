class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        can=0
        for i in range(len(nums)):
            if c==0:
                can=nums[i]
            if can==nums[i]:
                c+=1
            else:
                c-=1
        return can