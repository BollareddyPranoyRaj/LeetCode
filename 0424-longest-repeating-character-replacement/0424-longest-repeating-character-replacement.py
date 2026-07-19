class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct={}
        i=0
        res=0
        maxFreq=0
        for j in range(len(s)):
            dct[s[j]]=dct.get(s[j],0)+1
            maxFreq = max(maxFreq, dct[s[j]])
            if (j-i+1)-maxFreq<=k:
                res=max(res,(j-i+1))
            else:
                dct[s[i]]-=1
                i+=1
        return res


        