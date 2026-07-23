class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        c=1
        if n<=2:
            return n
        while c<=n:
            c<<=1
        return c