class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lst=[]
        add=0
        for x in nums:
            add+=x
            lst.append(add)
        if add-nums[0]==0 or len(nums)==0:
            return 0
        for i in range(1,len(lst)-1):
            left=lst[i-1]
            right=add-lst[i]
            if left==right:
                return i
        if lst[-2]==0:
            return len(lst)-1
        return -1
        