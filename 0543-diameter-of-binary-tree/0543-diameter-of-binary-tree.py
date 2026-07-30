# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=-1
        def helper(root):
            if not root:
                return 0
            l=helper(root.left)
            r=helper(root.right)
            self.maxi=max(self.maxi,l+r)
            return 1+max(l,r)
        helper(root)
        return self.maxi

        