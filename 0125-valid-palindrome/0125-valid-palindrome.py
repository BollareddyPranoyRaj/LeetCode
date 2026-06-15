class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for ch in s:
            if ch.isalnum():
                c+=ch
        c=c.lower()
        rev=c[::-1]
        if c==rev:
            return True
        return False
            

        