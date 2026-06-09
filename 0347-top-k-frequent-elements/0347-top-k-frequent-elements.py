class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh={}
        for x in nums:
            if x not in hsh:
                hsh[x] = 0
            hsh[x] += 1
        lst=[]
        for i in range(k):
            l=max(hsh.values())
            for j in hsh:
                if hsh[j]==l:
                    lst.append(j)
                    break
            hsh.pop(j)
        return lst


        