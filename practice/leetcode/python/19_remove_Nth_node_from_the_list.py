#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#Given the head of a linked list, remove the nth node from the end of the list and return its head^.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def removeNthNodeFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n <= 0 and head == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        if left.next:
            left.next = left.next.next
        return(dummy.next)


