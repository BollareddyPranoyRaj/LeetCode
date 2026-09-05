class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score=[0]*(n+1)
        if n==1:
            return 1
        for i in range(len(trust)):
            score[trust[i][0]]-=1
            score[trust[i][1]]+=1
        for i in range(len(score)):
            if score[i]==n-1:
                return i
        return -1
