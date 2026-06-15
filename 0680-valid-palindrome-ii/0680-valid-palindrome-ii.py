class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                a,b=s[l+1:r+1],s[l:r]
                return a==a[::-1] or b==b[::-1]
            l+=1
            r-=1
        return True


            
        