class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct={}
        st=[]
        for i in nums2:
            while st and st[-1]<i:
                num=st.pop()
                dct[num]=i
            st.append(i)
        lst=[]
        for i in nums1:
            if i not in dct:
                lst.append(-1)
            else:
                lst.append(dct[i])
        return lst
