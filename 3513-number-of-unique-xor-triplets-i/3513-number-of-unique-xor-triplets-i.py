class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        if n<=2:
            return n
        while n>0:
            n=n//2
            c+=1
        return pow(2,c)

        