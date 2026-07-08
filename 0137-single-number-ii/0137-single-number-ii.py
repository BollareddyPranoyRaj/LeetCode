class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hsh={}
        for i in nums:
            hsh[i]=hsh.get(i,0)+1
        for i in hsh:
            if hsh[i]==1:
                return i
        return -1
        

        