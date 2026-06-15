class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for ch in s:
            if ch.isalnum():
                c+=ch
        c=c.lower()
        return c==c[::-1]
            

        