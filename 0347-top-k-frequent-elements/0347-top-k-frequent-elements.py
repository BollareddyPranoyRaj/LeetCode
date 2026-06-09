class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for x in nums:
            count[x]=count.get(x,0)+1
        freq=[[] for _ in range(len(nums)+1)]
        for h,v in count.items():
            freq[v].append(h)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res


