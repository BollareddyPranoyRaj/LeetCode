class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # Merge two halves
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2