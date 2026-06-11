class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add=0
        lst=[]
        for x in nums:
            add+=x
            lst.append(add)
        return lst
        