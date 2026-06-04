class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        hsh={}
        for i in s:
            hsh[i]=hsh.get(i,0)+1
        for i in t:
            if i not in s:
                return False
            hsh[i]-=1
        for value in hsh.values():
            if value<0:
                return False
        return True