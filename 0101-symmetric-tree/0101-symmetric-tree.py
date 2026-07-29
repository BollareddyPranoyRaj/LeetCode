# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(p,q):
            if not p and not q:
                return True
            if not p and q or p and not q:
                return False
            if p.val!=q.val:
                return False
            l=helper(p.left,q.right)
            r=helper(p.right,q.left)
            if l and r:
                return True
            return False
        return helper(root.left,root.right)

        
        