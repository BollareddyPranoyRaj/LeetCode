class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=c2=0
        cand1=cand2=None
        for i in nums:
            if cand1==i:
                c1+=1
            elif cand2==i:
                c2+=1
            elif c1==0:
                cand1=i
                c1=1
            elif c2==0:
                cand2=i
                c2=1
            else:
                c1-=1
                c2-=1
        k=[]
        if nums.count(cand1)>len(nums)//3:
            k.append(cand1)
        if nums.count(cand2)>len(nums)//3:
            k.append(cand2)
        return k