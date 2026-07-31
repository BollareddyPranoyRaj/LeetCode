# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i=0
        self.ans=-1
        def inorder(root):
            if not root:
                return None
            l=inorder(root.left)            
            self.i+=1
            if self.i==k:
                self.ans=root.val
            r=inorder(root.right)
        inorder(root)
        return self.ans

        