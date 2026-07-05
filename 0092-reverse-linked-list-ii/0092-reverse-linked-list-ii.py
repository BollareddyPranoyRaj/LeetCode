# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        prefix=suffix=None
        for i in range(left-1):
            prefix=cur
            cur=cur.next
        curr=cur
        for j in range(right-left):
            curr=curr.next
        suffix=curr.next
        for j in range(right-left+1):
            newnode=cur.next
            cur.next=suffix
            suffix = cur
            cur=newnode
        if prefix:
            prefix.next=suffix
        else:
            head=suffix
        return head
        
        
        