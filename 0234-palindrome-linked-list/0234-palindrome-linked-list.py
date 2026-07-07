# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow
        slow=None
        prev= None 
        while curr:
            newNode=curr.next
            curr.next=prev
            prev=curr
            curr=newNode
        while head and prev:
            if head.val != prev.val:
                return False
            head=head.next
            prev=prev.next
        return True

        