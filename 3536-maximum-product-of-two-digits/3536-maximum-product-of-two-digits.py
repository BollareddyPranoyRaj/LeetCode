class Solution:
    def maxProduct(self, n: int) -> int:
        fmax=0
        smax=0
        while n!=0:
            m=n%10
            if m>fmax:
                smax=fmax
                fmax=m
            elif m>smax:
                smax=m
            n//=10
        return fmax*smax

