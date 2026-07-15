class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd,sumeven=0,0
        for i in range(2*n):
            if i % 2 == 0:
                sumeven+=i
            else:
                sumodd+=i
        return math.gcd(sumeven,sumodd)