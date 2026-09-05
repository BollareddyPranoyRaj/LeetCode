class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dct={}
        if n==1:
            return 1
        for i in range(len(trust)):
            dct[trust[i][0]] = dct.get(trust[i][0], 0) - 1
            dct[trust[i][1]] = dct.get(trust[i][1], 0) + 1
        maxi=-1
        k=-1
        for i,j in dct.items():
            if j>maxi:
                maxi=j
                k=i
        if maxi==n-1:
            return k
        else:
            return -1
        
