class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            sum1=0
            seen.add(n)
            while n>0:
                m=n%10
                sum1=sum1+m**2
                n=n//10
            n=sum1
        return n==1
        



        