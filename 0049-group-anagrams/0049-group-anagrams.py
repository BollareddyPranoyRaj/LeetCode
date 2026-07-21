class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh={}
        for i in strs:
            ele="".join(sorted(i))
            if ele not in hsh:
                hsh[ele]=[]
            hsh[ele].append(i)
        lst=[]
        for i in hsh.values():
            lst.append(i)
        return lst
            
        