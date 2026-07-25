class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def solve(l,r):
            if l>=r:
                return
            s[l],s[r]=s[r],s[l]
            solve(l+1,r-1)
        solve(0,len(s)-1)
        