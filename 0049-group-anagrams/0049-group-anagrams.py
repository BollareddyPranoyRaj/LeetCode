class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt={}
        for x in strs:
            y=" ".join(sorted(x))
            if y not in dt:
                dt[y]=[]
            dt[y].append(x)
        return list(dt.values())
            