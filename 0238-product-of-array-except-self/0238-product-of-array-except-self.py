class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=[]
        sf=[]
        mul=1
        for i in range(len(nums)):
            mul*=nums[i]
            pf.append(mul)
        mul=1
        for i in range(len(nums)-1,-1,-1):
            mul*=nums[i]
            sf.append(mul)
        sf.reverse()
        answer=[]
        for i in range(len(nums)):
            left = pf[i-1] if i>0 else 1
            right = sf[i+1] if i<len(nums)-1 else 1
            answer.append(left*right)
        return answer
            