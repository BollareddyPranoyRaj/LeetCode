class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        fmax = float('-inf')
        smax = float('-inf')
        tmax = float('-inf')

        fmin = float('inf')
        smin = float('inf')

        for n in nums:
            if n >= fmax:
                tmax = smax
                smax = fmax
                fmax = n
            elif n >= smax:
                tmax = smax
                smax = n
            elif n > tmax:
                tmax = n

            if n <= fmin:
                smin = fmin
                fmin = n
            elif n < smin:
                smin = n

        return max(fmax * smax * tmax, fmax * fmin * smin)