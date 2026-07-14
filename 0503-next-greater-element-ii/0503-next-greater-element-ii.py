class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        arr=[-1]*len(nums)
        for i in range(2*len(nums)):
            i=i%len(nums)
            while st and nums[st[-1]]<nums[i]:
                arr[st[-1]]=nums[i]
                st.pop()
            st.append(i)
        return arr