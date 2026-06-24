class Solution:
    def isValid(self, s: str) -> bool:
        dct={')':'(',']':'[','}':'{'}
        res=[]
        for i in range(len(s)):
            if s[i] in dct:
                if len(res)!=0 and res[-1]==dct[s[i]]:
                    res.pop()
                else:
                    return False
            else:
                res.append(s[i])
        return len(res)==0

        
    