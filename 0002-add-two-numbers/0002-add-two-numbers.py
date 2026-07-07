# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        carry=0
        curr=dummy
        while l1 and l2:
            val=l1.val+l2.val+carry
            carry=val//10
            val=val%10
            curr.next=ListNode(val)
            curr=curr.next
            l1=l1.next
            l2=l2.next
        while l1:
            if carry==1:
                val=l1.val+carry
                carry=val//10
                val=val%10
                curr.next=ListNode(val)
            else:
                curr.next=l1
            l1=l1.next
            curr=curr.next
        if carry==1:
            curr.next=ListNode(1)
        while l2:
            if carry==1:
                val=l2.val+carry
                carry=val//10
                val=val%10
                curr.next=ListNode(val)
            else:
                curr.next=l2
            l2=l2.next
            curr=curr.next
        if carry==1:
            curr.next=ListNode(1)
        return dummy.next
        