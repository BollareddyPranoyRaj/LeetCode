# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dare=dummy
        carry=0

        while l1 and l2:
            s=l1.val+l2.val+carry
            dummy.next=ListNode(s%10)
            carry=s//10
            l1=l1.next
            l2=l2.next
            dummy=dummy.next

        while l2:
            s = l2.val + carry
            dummy.next = ListNode(s % 10)
            carry = s // 10
            l2 = l2.next
            dummy = dummy.next

        while l1:
            s = l1.val + carry
            dummy.next = ListNode(s % 10)
            carry = s // 10
            l1 = l1.next
            dummy = dummy.next
        if carry:
            dummy.next=ListNode(1)
        return dare.next
        

        