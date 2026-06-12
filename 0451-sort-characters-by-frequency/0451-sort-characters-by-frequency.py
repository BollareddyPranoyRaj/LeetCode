class Solution:
    def frequencySort(self, s: str) -> str:
        dct={}
        for i in range(len(s)):
            dct[s[i]] = dct.get(s[i], 0) + 1
        lst=[]
        while dct:
            max_key=max(dct,key=dct.get)
            max_val=dct[max_key]
            while max_val>0:
                lst.append(max_key)
                max_val-=1
            dct.pop(max_key)
        return "".join(lst)
            

        
            
        