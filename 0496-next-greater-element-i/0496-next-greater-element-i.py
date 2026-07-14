class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            for j in range(len(nums2)):
                if i==nums2[j]:
                    saved=j
                    break
            flag=1
            for k in range(j+1,len(nums2)):
                if nums2[k]>i:
                    res.append(nums2[k])
                    flag=0
                    break
                flag=1
            if flag==1:
                res.append(-1)
        return res