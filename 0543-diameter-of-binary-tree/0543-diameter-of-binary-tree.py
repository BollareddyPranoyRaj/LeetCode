# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(root,res):
            if not root:
                return 0
            l=helper(root.left,self.res)
            r=helper(root.right,self.res)
            self.res=max(self.res,l+r)
            return 1+max(l,r)
        helper(root,self.res)
        return self.res

        