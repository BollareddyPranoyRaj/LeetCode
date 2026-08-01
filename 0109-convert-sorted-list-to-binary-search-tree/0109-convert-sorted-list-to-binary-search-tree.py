# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            slow=fast=head
            prev=None
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            mid=slow
            root=TreeNode(mid.val)
            prev.next=None
            Mid=slow.next
            root.left=helper(head)
            root.right=helper(Mid)
            return root
        return helper(head)
       